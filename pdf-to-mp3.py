import sys
import subprocess
import pkg_resources

# List of required packages with their PyPI names and versions
required_packages = [
    'PyPDF2==3.0.1',
    'pyttsx3==2.98',
    'pydub==0.25.1',
    'deep-translator==1.11.4',
    'gTTS==2.5.3',
    'requests==2.32.0',
    'moviepy==1.0.3',
    'reportlab==4.2.4',
    'langdetect==1.0.9',
    'argostranslate==1.9.6',
    'TTS==0.22.0',
    'torch==2.0.1',
    'libretranslatepy==2.1.1'
]

def install_missing_packages(packages):
    """
    Checks which packages from the list are missing and installs them using pip.
    """
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = []
    for package in packages:
        pkg_name = package.split('==')[0]
        if pkg_name.lower() not in installed:
            missing.append(package)
    
    if missing:
        print("Missing packages found. Installing...")
        try:
            # Use pip to install missing packages
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during package installation: {e}")
            sys.exit(1)
    else:
        print("All required packages are already installed.")

# Install missing packages before importing them
install_missing_packages(required_packages)

# Now import all necessary modules
import os
import glob
import PyPDF2
import re
import pyttsx3
from pydub import AudioSegment
from deep_translator import GoogleTranslator
from gtts import gTTS
import time
from requests.exceptions import HTTPError
import requests
import tempfile
import shutil
import uuid
import sys
import subprocess
import json
from datetime import datetime
from moviepy.editor import concatenate_audioclips, AudioFileClip
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import argostranslate.package
import argostranslate.translate
from TTS.api import TTS
import torch
# Import for LibreTranslate
# from libretranslatepy import LibreTranslateAPI

# Function to translate text using DeepL API
def translate_deepl(text, source_lang='EN', target_lang='PL'):
    DEEPL_API_KEY = "#DeepL API key#"  # Make sure to set your DeepL API key
    url = " https://api.deepl.com/v2/translate"
    headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"}
    data = {
        "text": text,
        "source_lang": source_lang.upper(),
        "target_lang": target_lang.upper()
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        result = response.json()
        return result['translations'][0]['text']
    except HTTPError as e:
        print(f"DeepL translation error: {e.response.status_code} - {e.response.text}")
        return text
    except Exception as e:
        print(f"Other error during DeepL translation: {e}")
        return text

# Function to translate text using Google Translator
def translate_google(text, source_lang='en', target_lang='pl'):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"Google translation error: {e}")
        return text

# Function to translate text using Argos Translate
def translate_argos(text, source_lang='en', target_lang='pl'):
    language_map = {
        'en': 'en',
        'pl': 'pl',
        'uk': 'uk'
    }
    source_lang_code = language_map.get(source_lang, 'en')
    target_lang_code = language_map.get(target_lang, 'pl')

    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = next((lang for lang in installed_languages if lang.code == source_lang_code), None)
    to_lang = next((lang for lang in installed_languages if lang.code == target_lang_code), None)

    if from_lang is None or to_lang is None:
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next((package for package in available_packages if package.from_code == source_lang_code and package.to_code == target_lang_code), None)
        if package_to_install is not None:
            print(f"Downloading and installing translation package from {source_lang_code} to {target_lang_code}...")
            download_path = package_to_install.download()
            argostranslate.package.install_from_path(download_path)
            installed_languages = argostranslate.translate.get_installed_languages()
            from_lang = next((lang for lang in installed_languages if lang.code == source_lang_code), None)
            to_lang = next((lang for lang in installed_languages if lang.code == target_lang_code), None)
        else:
            print(f"No translation package found from {source_lang_code} to {target_lang_code}.")
            return text

    translation = from_lang.get_translation(to_lang)
    return translation.translate(text)

# Function to translate text using LibreTranslate API
def translate_libretranslate(text, source_lang='en', target_lang='pl'):
    url = "https://libretranslate.de/translate"
    payload = {
        'q': text,
        'source': source_lang,
        'target': target_lang,
        'format': 'text'
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        result = response.json()
        return result['translatedText']
    except Exception as e:
        print(f"Error during LibreTranslate translation: {e}")
        return text

# Function to create a translated PDF
def save_translated_pdf(text, output_pdf_path):
    try:
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        width, height = letter
        lines = text.split('\n')
        y = height - 40
        max_lines_per_page = 40
        line_count = 0

        for line in lines:
            c.setFont('DejaVuSans', 12)
            wrapped_lines = wrap_text(line, 80)
            for wrapped_line in wrapped_lines:
                c.drawString(40, y, wrapped_line)
                y -= 15
                line_count += 1
                if line_count >= max_lines_per_page:
                    c.showPage()
                    y = height - 40
                    line_count = 0
                    c.setFont('DejaVuSans', 12)
        c.save()
    except Exception as e:
        print(f"Error saving translated PDF: {e}")

# Function to wrap text to a specified length
def wrap_text(text, max_chars):
    words = text.split()
    wrapped_lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars:
            current_line += " " + word if current_line else word
        else:
            wrapped_lines.append(current_line)
            current_line = word
    if current_line:
        wrapped_lines.append(current_line)
    return wrapped_lines

# Function to choose translation method
def get_translation_method():
    print("Choose translation engine:")
    print("1. Google Translator")
    print("2. DeepL")
    print("3. Argos Translate (local translation model)")
    print("4. LibreTranslate")
    method_choice = input("Enter the number of the translation engine (1, 2, 3, or 4): ")
    if method_choice == '2':
        return 'deepl'
    elif method_choice == '3':
        return 'argos'
    elif method_choice == '4':
        return 'libretranslate'
    else:
        return 'google'

# Main function for translating text
def translate_text(text, method='google', source_lang='en', target_lang='pl'):
    if method == 'deepl':
        return translate_deepl(text, source_lang=source_lang, target_lang=target_lang)
    elif method == 'argos':
        return translate_argos(text, source_lang=source_lang, target_lang=target_lang)
    elif method == 'libretranslate':
        return translate_libretranslate(text, source_lang=source_lang, target_lang=target_lang)
    else:
        return translate_google(text, source_lang=source_lang, target_lang=target_lang)

# Main function to convert PDF to MP3
def PdfConverter():
    def create_folder(folder_name):
        folder_path = os.path.join(os.getcwd(), folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    # Create folders for PDFs, MP3s, and translated PDFs
    pdf_folder = create_folder('pdf')
    mp3_folder = create_folder('mp3')
    translated_pdf_folder = create_folder('translated_pdf')
    tts_model = None
    device = "cuda" if torch.cuda.is_available() else "cpu"

    while True:
        # Get list of PDF files to process
        pdf_files = glob.glob(os.path.join(pdf_folder, '*.pdf'))
        if not pdf_files:
            print('No PDF files found for conversion.')
            input("Press any key to continue...")
            return

        print('List of PDF files:')
        for i, file_path in enumerate(pdf_files, 1):
            print(f'{i}. {os.path.basename(file_path)}')

        # User selects which PDF file(s) to process
        file_input = input('\nEnter the number of the PDF file to convert to MP3, enter "A" to process all files, or enter "0" to exit: ').strip()
        if file_input.lower() == 'a':
            files_to_process = pdf_files
            translation_choice = get_translation_method()
        elif file_input == '0':
            print("No file selected. Exiting program.")
            input("Press any key to exit...")
            return
        else:
            try:
                file_number = int(file_input)
                if 1 <= file_number <= len(pdf_files):
                    files_to_process = [pdf_files[file_number - 1]]
                    translation_choice = get_translation_method()
                else:
                    print(f'The number must be between 1 and {len(pdf_files)}.')
                    continue
            except ValueError:
                print('Invalid choice. Please try again.')
                continue

        # User selects playback language
        print('Choose playback language: 1. English, 2. Polish, 3. Ukrainian, 4. Detect automatically.')
        language_choice = input('Enter the language number: ').strip()
        language_map = {'1': 'en', '2': 'pl', '3': 'uk'}
        language = language_map.get(language_choice) if language_choice != '4' else None
        print(f"Selected language: {language if language else 'Automatic detection'}")

        # Detect language if user selected automatic detection
        if language_choice == '4':
            try:
                with open(files_to_process[0], 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    if len(pdf_reader.pages) > 0:
                        page_text = pdf_reader.pages[0].extract_text()
                        language = detect(page_text) if page_text else 'en'
                        print(f"Automatically detected language: {language}")
                    else:
                        print("PDF contains no pages. Using default language 'en'.")
                        language = 'en'
            except Exception as e:
                print(f"Failed to detect language: {e}")
                language = 'en'

        # User selects TTS engine
        print('Choose TTS engine:')
        print('1. gTTS (requires internet)')
        print('2. pyttsx3 (works offline, lower quality)')
        print('3. Coqui TTS (high quality, works locally)')
        tts_choice = input('Enter the number of the TTS engine: ').strip()
        tts_engine = {'1': 'gtts', '2': 'pyttsx3', '3': 'coqui'}.get(tts_choice)

        # Initialize Coqui TTS model if selected
        if tts_engine == 'coqui' and tts_model is None:
            try:
                model_name = 'tts_models/multilingual/multi-dataset/your_tts'
                print(f"Loading Coqui TTS model: {model_name}")
                tts_model = TTS(model_name).to(device)
                speaker_idx = tts_model.speakers[0]  # Choose the first speaker
            except Exception as e:
                print(f"Error initializing Coqui TTS: {e}")
                return

        temp_dir = tempfile.mkdtemp(prefix='pdf_to_mp3_')
        try:
            for pdf_file in files_to_process:
                print(f"\nProcessing file: {os.path.basename(pdf_file)}")
                if not os.path.isfile(pdf_file):
                    print(f"File {pdf_file} does not exist. Skipping...")
                    continue

                # Generate translated PDF file name
                translator_name = {
                    'google': 'GoogleTranslator',
                    'deepl': 'DeepL',
                    'argos': 'Argos Translate',
                    'libretranslate': 'LibreTranslate'
                }.get(translation_choice)
                translated_pdf_name = f"{os.path.splitext(os.path.basename(pdf_file))[0]} [{translator_name}, {language}].pdf"
                translated_pdf_path = os.path.join(translated_pdf_folder, translated_pdf_name)

                if os.path.exists(translated_pdf_path):
                    print(f"Translated PDF already exists: {translated_pdf_name}")
                    with open(translated_pdf_path, 'rb') as f:
                        pdf_reader = PyPDF2.PdfReader(f)
                        text = ''.join([page.extract_text() for page in pdf_reader.pages if page.extract_text()]).strip()
                    # Since we have the translated text, we can proceed to create the audio
                else:
                    # Extract text from PDF and translate
                    with open(pdf_file, 'rb') as f:
                        pdf_reader = PyPDF2.PdfReader(f)
                        pages_text = [page.extract_text().strip().replace("\n", " ") for page in pdf_reader.pages]
                        text = ' '.join(pages_text).strip()

                    try:
                        detected_language = detect(text)
                        print(f"Detected PDF language: {detected_language}")
                    except LangDetectException:
                        print("Failed to detect text language. Assuming 'en'.")
                        detected_language = 'en'

                    if detected_language.startswith(language):
                        print("Source language is the same as the target language. Skipping translation.")
                        # No translation needed; proceed with the original text
                    else:
                        print("Translating text...")
                        max_chunk_size = 1000
                        text_chunks = wrap_text(text, max_chunk_size)
                        translated_text = ''.join([
                            translate_text(
                                chunk,
                                method=translation_choice,
                                source_lang=detected_language,
                                target_lang=language
                            ) + ' ' for chunk in text_chunks
                        ]).strip()
                        save_translated_pdf(translated_text, translated_pdf_path)
                        print(f"Translated PDF saved: {translated_pdf_name}")
                        text = translated_text

                # Create audio file from text
                print("Creating audio file. Please wait...")
                tts_max_length = 500 if tts_engine == 'coqui' else 4999
                audio_text_chunks = wrap_text(text, tts_max_length)
                audio_chunks = []

                for idx, text_chunk in enumerate(audio_text_chunks, 1):
                    if not text_chunk:
                        print(f"Skipping empty text chunk {idx}")
                        continue
                    try:
                        temp_file = os.path.join(temp_dir, f"temp_{uuid.uuid4()}.mp3")
                        if tts_engine == 'gtts':
                            # Retry mechanism for Google TTS due to any error
                            retries, max_retries, wait_time_after_reconnect, wait_time_before_retry, success = 0, 20, 20, 2, False
                            while not success and retries < max_retries:
                                try:
                                    tts = gTTS(text=text_chunk, lang=language if language else 'en', slow=False)
                                    tts.save(temp_file)
                                    success = True
                                    time.sleep(1)
                                except Exception as e:
                                    retries += 1
                                    print(f"Error encountered: {e}")
                                    print(f"Retrying {retries}/{max_retries} after reconnecting VPN...")
                                    reconnect_vpn()
                                    time.sleep(wait_time_after_reconnect)
                                    print(f"Waiting {wait_time_before_retry} seconds before next attempt...")
                                    time.sleep(wait_time_before_retry)
                            if not success:
                                print(f"Failed to process after {max_retries} attempts.")
                                continue
                            else:
                                print("TTS synthesis completed successfully.")
                        elif tts_engine == 'pyttsx3':
                            engine = pyttsx3.init()
                            engine.setProperty('rate', 150)
                            voice_set = False
                            # Set voice based on the selected language
                            for voice in engine.getProperty('voices'):
                                if language == 'pl' and ('polish' in voice.name.lower() or 'pl' in voice.id.lower()):
                                    engine.setProperty('voice', voice.id)
                                    voice_set = True
                                    break
                                elif language == 'en' and ('english' in voice.name.lower() or 'en' in voice.id.lower()):
                                    engine.setProperty('voice', voice.id)
                                    voice_set = True
                                    break
                                elif language == 'uk' and ('ukrainian' in voice.name.lower() or 'uk' in voice.id.lower()):
                                    engine.setProperty('voice', voice.id)
                                    voice_set = True
                                    break
                            if not voice_set:
                                print(f"No voice found for language {language}. Using default voice.")
                            engine.save_to_file(text_chunk, temp_file)
                            engine.runAndWait()
                        elif tts_engine == 'coqui':
                            temp_file_wav = os.path.join(temp_dir, f"temp_{uuid.uuid4()}.wav")
                            tts_model.tts_to_file(text=text_chunk, file_path=temp_file_wav, language=language, speaker=speaker_idx)
                            sound = AudioSegment.from_wav(temp_file_wav)
                            sound.export(temp_file, format="mp3")
                            os.remove(temp_file_wav)
                        audio_chunks.append(temp_file)
                    except Exception as e:
                        print(f"Error during speech synthesis for text chunk: {e}")

                if not audio_chunks:
                    print("No audio chunks were generated.")
                    continue

                # Concatenate all audio chunks into a final MP3 file
                print("Merging audio chunks...")
                try:
                    audio_clips = [AudioFileClip(chunk) for chunk in audio_chunks]
                    final_audio = concatenate_audioclips(audio_clips)
                    base_name = os.path.splitext(os.path.basename(pdf_file))[0] + f' [{translator_name}, {language}, {tts_engine}].mp3'
                    mp3_file_path = os.path.join(mp3_folder, base_name)
                    counter = 1
                    while os.path.exists(mp3_file_path):
                        mp3_file_name = f"{os.path.splitext(base_name)[0]}_{counter}.mp3"
                        mp3_file_path = os.path.join(mp3_folder, mp3_file_name)
                        counter += 1
                    final_audio.write_audiofile(mp3_file_path, codec='mp3')
                    print(f'File {base_name} was successfully created in the mp3 folder.\n')
                except Exception as e:
                    print(f"Error merging audio files using moviepy: {e}")
                finally:
                    for clip in audio_clips:
                        clip.close()
        finally:
            shutil.rmtree(temp_dir)

        # User decides whether to process another file or exit
        while True:
            try:
                choice_result = int(input('Choose: 1. Process again, 2. Exit: ').strip())
                if choice_result == 1:
                    break
                elif choice_result == 2:
                    print("Exiting program.")
                    input("Press any key to exit...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid number. Please try again.")

# Function to disconnect and reconnect VPN (no feedback waiting)
def reconnect_vpn():
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Disconnecting from VPN...")
        subprocess.run([r"C:\Program Files\NordVPN\nordvpn.exe", "--disconnect"], check=False)
        
        print(f"Waiting 20 seconds before reconnecting...")
        time.sleep(20)  # Wait 20 seconds before reconnecting
        
        print(f"[{current_time}] Reconnecting to VPN...")
        subprocess.run([r"C:\Program Files\NordVPN\nordvpn.exe", "--connect"], check=False)
    except Exception as e:
        print(f"Error managing VPN: {e}")

if __name__ == '__main__':
    PdfConverter()

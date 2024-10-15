# PDF to MP3 Converter with Translation and TTS Support

## English

### Description

This Python script converts PDF files into MP3 audio files with support for translation and text-to-speech (TTS). It allows users to select PDF files from a folder, choose a translation engine, select the target language, and pick a TTS engine to generate audio files from the text extracted from PDFs.

### Features

- **PDF to MP3 Conversion**: Convert your PDF documents into audio files.
- **Multiple Translation Engines**:
  - Google Translator
  - DeepL
  - Argos Translate (local translation model)
  - LibreTranslate
- **Multiple TTS Engines**:
  - gTTS (Google Text-to-Speech)
  - pyttsx3 (offline TTS)
  - Coqui TTS (high-quality local TTS)
- **Language Detection**: Automatically detect the language of the PDF.
- **VPN Reconnection**: Automatically reconnects NordVPN if translation requests fail due to rate limiting.

### Requirements

- **Python**: Version 3.6 or higher.
- **Internet Connection**: Required for translation and TTS engines that use online services.
- **NordVPN**: If you intend to use the VPN reconnection feature.
- **Python Packages**: The script will automatically install the following if they are missing:
  - PyPDF2==3.0.1
  - pyttsx3==2.98
  - pydub==0.25.1
  - deep-translator==1.11.4
  - gTTS==2.5.3
  - requests==2.32.0
  - moviepy==1.0.3
  - reportlab==4.2.4
  - langdetect==1.0.9
  - argostranslate==1.9.6
  - TTS==0.22.0
  - torch==2.0.1
  - libretranslatepy==2.1.1

### Installation

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. **Navigate to the Directory**

   ```bash
   cd your_repository
   ```

3. **Ensure Python is Installed**

   Verify that Python 3.6 or higher is installed:

   ```bash
   python --version
   ```

4. **Install Required Packages**

   The script will automatically check and install missing packages. Alternatively, you can install them manually:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up API Keys and Models**

   - **DeepL API Key**: If you plan to use DeepL for translation, obtain an API key from [DeepL Developer](https://www.deepl.com/pro-api) and replace `"YOUR_DEEPL_API_KEY"` in the script with your key.
   - **Coqui TTS Model**: If using Coqui TTS, ensure you have the necessary model downloaded. The script uses `'tts_models/multilingual/multi-dataset/your_tts'` by default.
   - **NordVPN CLI**: If using the VPN reconnection feature, ensure NordVPN CLI is installed and accessible at `C:\Program Files\NordVPN\nordvpn.exe`.

### Usage

1. **Prepare PDF Files**

   Place the PDF files you wish to convert in the `pdf` folder within the script's directory.

2. **Run the Script**

   ```bash
   python your_script_name.py
   ```

3. **Follow the Prompts**

   - **Select PDF Files**: Choose a single file or all files for conversion.
   - **Choose Translation Engine**: Select from Google Translator, DeepL, Argos Translate, or LibreTranslate.
   - **Select Target Language**: Options are English, Polish, Ukrainian, or automatic detection.
   - **Choose TTS Engine**: Select from gTTS, pyttsx3, or Coqui TTS.

4. **Wait for Processing**

   The script will:

   - Extract text from the PDFs.
   - Detect the language (if automatic detection is selected).
   - Translate the text (if required).
   - Generate MP3 audio files using the chosen TTS engine.
   - Save translated PDFs in the `translated_pdf` folder.

5. **Find Your Files**

   - MP3 files will be saved in the `mp3` folder.
   - Translated PDFs will be in the `translated_pdf` folder.

### Notes

- **API Keys**

  - **DeepL**: Remember to replace `"YOUR_DEEPL_API_KEY"` in the script with your actual DeepL API key.

- **VPN Reconnection**

  - Ensure NordVPN is installed and the CLI is accessible if you intend to use the VPN reconnection feature.

- **Language Detection**

  - The script uses `langdetect` to automatically detect the language if you select the automatic detection option.

- **Performance**

  - Using Coqui TTS and large PDF files may require significant processing time and resources.

### License

This project is licensed under the MIT License.

---

## Polski

### Opis

Ten skrypt w języku Python konwertuje pliki PDF na pliki audio MP3 z obsługą tłumaczenia i syntezy mowy (TTS). Umożliwia użytkownikom wybór plików PDF z folderu, wybór silnika tłumaczenia, docelowego języka oraz silnika TTS do generowania plików audio z tekstu wyodrębnionego z PDF.

### Funkcje

- **Konwersja PDF do MP3**: Przekształć swoje dokumenty PDF w pliki audio.
- **Wiele silników tłumaczenia**:
  - Google Translator
  - DeepL
  - Argos Translate (lokalny model tłumaczenia)
  - LibreTranslate
- **Wiele silników TTS**:
  - gTTS (Google Text-to-Speech)
  - pyttsx3 (offline TTS)
  - Coqui TTS (wysokiej jakości lokalny TTS)
- **Wykrywanie języka**: Automatycznie wykrywa język pliku PDF.
- **Ponowne łączenie VPN**: Automatycznie ponownie łączy NordVPN, jeśli żądania tłumaczenia nie powiodą się z powodu limitów.

### Wymagania

- **Python**: Wersja 3.6 lub wyższa.
- **Połączenie z Internetem**: Wymagane dla silników tłumaczenia i TTS korzystających z usług online.
- **NordVPN**: Jeśli zamierzasz używać funkcji ponownego łączenia VPN.
- **Pakiety Pythona**: Skrypt automatycznie zainstaluje poniższe pakiety, jeśli ich brakuje:
  - PyPDF2==3.0.1
  - pyttsx3==2.98
  - pydub==0.25.1
  - deep-translator==1.11.4
  - gTTS==2.5.3
  - requests==2.32.0
  - moviepy==1.0.3
  - reportlab==4.2.4
  - langdetect==1.0.9
  - argostranslate==1.9.6
  - TTS==0.22.0
  - torch==2.0.1
  - libretranslatepy==2.1.1

### Instalacja

1. **Sklonuj lub pobierz repozytorium**

   ```bash
   git clone https://github.com/twoja_nazwa_uzytkownika/twoje_repozytorium.git
   ```

2. **Przejdź do katalogu**

   ```bash
   cd twoje_repozytorium
   ```

3. **Upewnij się, że Python jest zainstalowany**

   Sprawdź, czy Python w wersji 3.6 lub wyższej jest zainstalowany:

   ```bash
   python --version
   ```

4. **Zainstaluj wymagane pakiety**

   Skrypt automatycznie sprawdzi i zainstaluje brakujące pakiety. Alternatywnie możesz je zainstalować ręcznie:

   ```bash
   pip install -r requirements.txt
   ```

5. **Skonfiguruj klucze API i modele**

   - **Klucz API DeepL**: Jeśli planujesz używać DeepL do tłumaczenia, uzyskaj klucz API z [DeepL Developer](https://www.deepl.com/pro-api) i zastąp w skrypcie `"YOUR_DEEPL_API_KEY"` swoim kluczem.
   - **Model Coqui TTS**: Jeśli używasz Coqui TTS, upewnij się, że masz pobrany odpowiedni model. Skrypt domyślnie używa `'tts_models/multilingual/multi-dataset/your_tts'`.
   - **NordVPN CLI**: Jeśli używasz funkcji ponownego łączenia VPN, upewnij się, że NordVPN CLI jest zainstalowany i dostępny pod `C:\Program Files\NordVPN\nordvpn.exe`.

### Użycie

1. **Przygotuj pliki PDF**

   Umieść pliki PDF, które chcesz przekonwertować, w folderze `pdf` w katalogu skryptu.

2. **Uruchom skrypt**

   ```bash
   python nazwa_skryptu.py
   ```

3. **Postępuj zgodnie z instrukcjami**

   - **Wybierz pliki PDF**: Wybierz pojedynczy plik lub wszystkie pliki do konwersji.
   - **Wybierz silnik tłumaczenia**: Wybierz spośród Google Translator, DeepL, Argos Translate lub LibreTranslate.
   - **Wybierz docelowy język**: Dostępne opcje to angielski, polski, ukraiński lub automatyczne wykrywanie.
   - **Wybierz silnik TTS**: Wybierz spośród gTTS, pyttsx3 lub Coqui TTS.

4. **Poczekaj na przetwarzanie**

   Skrypt:

   - Wyodrębni tekst z plików PDF.
   - Wykryje język (jeśli wybrano automatyczne wykrywanie).
   - Przetłumaczy tekst (jeśli to konieczne).
   - Wygeneruje pliki MP3 za pomocą wybranego silnika TTS.
   - Zapisze przetłumaczone pliki PDF w folderze `translated_pdf`.

5. **Znajdź swoje pliki**

   - Pliki MP3 zostaną zapisane w folderze `mp3`.
   - Przetłumaczone pliki PDF będą w folderze `translated_pdf`.

### Uwagi

- **Klucze API**

  - **DeepL**: Pamiętaj, aby zastąpić `"YOUR_DEEPL_API_KEY"` w skrypcie swoim rzeczywistym kluczem API DeepL.

- **Ponowne łączenie VPN**

  - Upewnij się, że NordVPN jest zainstalowany, a CLI jest dostępne, jeśli zamierzasz używać funkcji ponownego łączenia VPN.

- **Wykrywanie języka**

  - Skrypt używa `langdetect` do automatycznego wykrywania języka, jeśli wybierzesz opcję automatycznego wykrywania.

- **Wydajność**

  - Używanie Coqui TTS i dużych plików PDF może wymagać znacznego czasu przetwarzania i zasobów.

### Licencja

Ten projekt jest licencjonowany na warunkach licencji MIT.

---

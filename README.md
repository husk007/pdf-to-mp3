# Instrukcja obsługi skryptu PDF to MP3 Converter

## Wymagania wstępne

Przed uruchomieniem skryptu upewnij się, że masz zainstalowane następujące oprogramowanie i biblioteki:

- Python 3.6 lub wyższy
- Biblioteki wymienione w pliku `requirements.txt`
- `ffmpeg` (wymagany przez biblioteki `pydub` i `moviepy`)
- (Opcjonalnie) `NordVPN` lub inny klient VPN, jeśli korzystasz z funkcji `reconnect_vpn`

## Instalacja

1. Zainstaluj wymagane biblioteki, uruchamiając w terminalu:

pip install -r requirements.txt


2. Upewnij się, że `ffmpeg` jest zainstalowany i dostępny w zmiennej środowiskowej `PATH`. Możesz pobrać `ffmpeg` z [oficjalnej strony](https://ffmpeg.org/download.html).

## Konfiguracja

1. Umieść pliki PDF do konwersji w folderze `pdf` w katalogu, w którym znajduje się skrypt.

2. W skrypcie uzupełnij klucz API dla DeepL, jeśli planujesz korzystać z tego tłumacza:

```python
DEEPL_API_KEY = "TWÓJ_KLUCZ_API_DEEPL"


## Użycie

Uruchom skrypt:

python pdf-to-mp3-all.py

Postępuj zgodnie z instrukcjami wyświetlanymi w terminalu:

Wybierz plik PDF do konwersji lub opcję przetworzenia wszystkich plików.
Wybierz silnik tłumaczenia (Google Translator, DeepL, Argos Translate).
Wybierz język odtwarzania lub opcję automatycznego wykrywania języka.
Wybierz silnik TTS (gTTS, pyttsx3, Coqui TTS).
Po zakończeniu działania skryptu przetłumaczone pliki PDF znajdziesz w folderze translated_pdf, a pliki MP3 w folderze mp3.

## Uwagi

gTTS wymaga połączenia z internetem i może napotkać ograniczenia liczby żądań. Skrypt zawiera mechanizm ponawiania próśb oraz opcjonalne przełączanie VPN.
pyttsx3 działa offline, ale jakość generowanego głosu może być niższa.
Coqui TTS oferuje wysoką jakość syntezy mowy i działa lokalnie, ale wymaga więcej zasobów systemowych.

## Problemy i wsparcie
Jeśli napotkasz problemy podczas korzystania ze skryptu, upewnij się, że wszystkie wymagane biblioteki są poprawnie zainstalowane i że korzystasz z odpowiedniej wersji Pythona. W razie pytań lub problemów skontaktuj się z autorem skryptu.
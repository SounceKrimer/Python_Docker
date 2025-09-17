import os
from google.cloud import translate_v2 as translate

# Встановити шлях до файлу ключа
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"googlekey.json"

translator = translate.Client()

# --- Функція перекладу ---
def TransLate(text: str, lang: str) -> str:
    try:
        # Переклад тексту
        result = translator.translate(text, target_language=lang.lower())
        return result['translatedText']
    except Exception as e:
        return f"Помилка перекладу: {e}"

# --- Клас для результату детекції ---
class Detected:
    def __init__(self, lang, confidence):
        self.lang = lang
        self.confidence = confidence
    def __repr__(self):
        return f"Detected(lang={self.lang}, confidence={self.confidence})"

# --- Функція визначення мови ---
def LangDetect(txt: str):
    try:
        detected = translator.detect_language(txt)
        return Detected(detected['language'], round(detected.get('confidence', 1), 2))
    except Exception as e:
        return Detected("unknown", 0.0)

# --- Функція для коду мови або назви ---
def CodeLang(lang: str) -> str:
    languages = translator.get_languages()
    lang_lower = lang.lower()
    for l in languages:
        if lang_lower == l['name'].lower():
            return l['language']
        elif lang_lower == l['language']:
            return l['name']
    return "Мову не знайдено!"

# --- Основна частина програми ---
if __name__ == "__main__":
    txt = input("Введіть текст для перекладу: ")
    lang = input("Введіть код або назву цільової мови (англійською): ")

    print("\nВведений текст:", txt)
    detected_language = LangDetect(txt)
    print("Виявлена мова:", detected_language)
    print("Переклад:", TransLate(txt, lang))
    print("Назва мови для коду/назви:", CodeLang(lang))

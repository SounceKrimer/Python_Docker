from googletrans import Translator, LANGUAGES

translator = Translator()

# --- Допоміжні функції ---
def TransLate(text: str, lang: str) -> str:
    lang_lower = lang.lower()
    lang_code = None
    for code, name in LANGUAGES.items():
        if lang_lower == name.lower() or lang_lower == code.lower():
            lang_code = code
            break
    if not lang_code:
        return "Мову не знайдено!"
    result = translator.translate(text, dest=lang_code)
    return result.text

class Detected:
    def __init__(self, lang, confidence):
        self.lang = lang
        self.confidence = confidence
    def __repr__(self):
        return f"Detected(lang={self.lang}, confidence={self.confidence})"

def LangDetect(txt: str):
    detected = translator.detect(txt)
    return Detected(detected.lang, round(detected.confidence, 2))

def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    for code, name in LANGUAGES.items():
        if lang_lower == name.lower():
            return code
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower].capitalize()
    return "Мову не знайдено!"

# --- Основна програма з консолі ---
txt = input("Введіть текст для перекладу: ")
lang = input("Введіть код або назву мови: ")

print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang("En"))
print(CodeLang("English"))

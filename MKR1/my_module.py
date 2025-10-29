# my_module.py
import json

def translate(text, lang="uk"):
    """Проста функція перекладу інтерфейсу."""
    translations = {
        "uk": {
            "lang_name": "Українська",
            "numbers_prompt": "Три числа a, b, c:",
            "result": "Результат:",
        },
        "en": {
            "lang_name": "English",
            "numbers_prompt": "Three numbers a, b, c:",
            "result": "Result:",
        }
    }
    # якщо мова не uk/en → українська
    if lang not in translations:
        lang = "uk"
    return translations[lang].get(text, text)


def process_numbers(a, b, c):
    """Додатні числа звести в квадрат, від’ємні залишити без змін."""
    nums = [a, b, c]
    processed = [x**2 if x > 0 else x for x in nums]
    return processed


def compare_mods(nums):
    """Порівняння модулів чисел і формування рядка типу |4| = |-4| < |9|"""
    mods = [abs(x) for x in nums]
    pairs = list(zip(mods, nums))
    pairs.sort(key=lambda x: x[0])  # сортуємо за модулем

    result_parts = [f"|{pairs[0][1]}|"]
    for i in range(1, len(pairs)):
        if pairs[i][0] == pairs[i - 1][0]:
            result_parts.append(f"= |{pairs[i][1]}|")
        else:
            result_parts.append(f"< |{pairs[i][1]}|")

    return " ".join(result_parts)

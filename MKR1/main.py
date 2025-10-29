# main.py
import json
import os
from my_module import translate, process_numbers, compare_mods

DATA_FILE = "MyData.json"

def read_data():
    """Зчитування даних з файлу MyData.json"""
    if not os.path.exists(DATA_FILE):
        return None
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # перевірка наявності всіх полів
            if not all(k in data for k in ["a", "b", "c", "lang"]):
                return None
            return data
    except Exception:
        return None


def write_data(a, b, c, lang):
    """Запис даних до файлу MyData.json"""
    data = {"a": a, "b": b, "c": c, "lang": lang}
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    data = read_data()

    if data is None:
        # Приклад 1: файлу немає або він некоректний
        print("Введіть три числа a, b, c:", end=" ")
        a, b, c = map(int, input().split())
        lang = input("Введіть мову інтерфейсу (uk/en): ").strip()
        write_data(a, b, c, lang)
        print(f"Дані збережено в файл {DATA_FILE}")
        return

    # Приклад 2: успішне читання даних
    lang = data.get("lang", "uk")
    print(f"Мова: {translate('lang_name', lang)}")

    a, b, c = data["a"], data["b"], data["c"]
    print(f"{translate('numbers_prompt', lang)} {a} {b} {c}")

    nums = process_numbers(a, b, c)
    print(" ".join(map(str, nums)))

    comparison = compare_mods(nums)
    print(comparison)


if __name__ == "__main__":
    main()

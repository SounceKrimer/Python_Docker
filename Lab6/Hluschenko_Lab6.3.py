import csv
from datetime import datetime, date
import os
import matplotlib.pyplot as plt

csv_filename = "Lab6/people_data.csv"

# Функція для обчислення віку
def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str.strip(), "%d.%m.%Y").date()
    except ValueError:
        return None
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Вікові категорії
def get_age_category(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 46 <= age <= 70:
        return "45-70"
    else:
        return "older_70"

try:
    if not os.path.exists(csv_filename):
        print(f"Помилка: файл CSV '{csv_filename}' не знайдено або неможливо відкрити.")
        exit(1)

    with open(csv_filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)

    print("Ok")

except Exception as e:
    print(f"Помилка при відкритті CSV файлу: {e}")
    exit(1)

# --- Підрахунки ---
sex_counts = {"Чоловіча": 0, "Жіноча": 0}
age_category_counts = {"younger_18": 0, "18-45": 0, "45-70": 0, "older_70": 0}
sex_age_counts = {
    "younger_18": {"Чоловіча": 0, "Жіноча": 0},
    "18-45": {"Чоловіча": 0, "Жіноча": 0},
    "45-70": {"Чоловіча": 0, "Жіноча": 0},
    "older_70": {"Чоловіча": 0, "Жіноча": 0}
}

for row in rows:
    sex = row.get("Стать", "").strip()
    birth_str = row.get("Дата народження", "").strip()
    age = calculate_age(birth_str)
    if age is None or sex not in ["Чоловіча", "Жіноча"]:
        continue

    # Стать
    sex_counts[sex] += 1

    # Вікова категорія
    category = get_age_category(age)
    age_category_counts[category] += 1

    # Стать × вікова категорія
    sex_age_counts[category][sex] += 1

# --- Вивід у консоль ---
print("\nКількість співробітників за статтю:")
for k, v in sex_counts.items():
    print(f"{k}: {v}")

print("\nКількість співробітників за віковими категоріями:")
for k, v in age_category_counts.items():
    print(f"{k}: {v}")

print("\nКількість співробітників за статтю та віковою категорією:")
for cat, data in sex_age_counts.items():
    print(f"{cat}: {data}")

# --- Побудова діаграм ---
# 1. Стать
plt.figure(figsize=(6,6))
plt.pie(sex_counts.values(), labels=sex_counts.keys(), autopct='%1.1f%%', colors=['skyblue','pink'])
plt.title("Розподіл співробітників за статтю")
plt.show()

# 2. Вікові категорії
plt.figure(figsize=(6,6))
plt.bar(age_category_counts.keys(), age_category_counts.values(), color='lightgreen')
plt.title("Кількість співробітників за віковими категоріями")
plt.ylabel("Кількість")
plt.show()

# 3. Стать × вікова категорія
categories = list(sex_age_counts.keys())
male_counts = [sex_age_counts[cat]["Чоловіча"] for cat in categories]
female_counts = [sex_age_counts[cat]["Жіноча"] for cat in categories]

plt.figure(figsize=(8,6))
bar_width = 0.35
x = range(len(categories))
plt.bar(x, male_counts, width=bar_width, label='Чоловіча', color='skyblue')
plt.bar([i + bar_width for i in x], female_counts, width=bar_width, label='Жіноча', color='pink')
plt.xticks([i + bar_width/2 for i in x], categories)
plt.ylabel("Кількість")
plt.title("Співробітники за статтю та віковою категорією")
plt.legend()
plt.show()

from faker import Faker
import csv
import random
import os
from datetime import date

# Ініціалізація Faker з українською локалізацією
fake = Faker(locale='uk_UA')

# Словники по батькові
male_middle_names = [
    "Іванович", "Петрович", "Сергійович", "Олександрович", "Володимирович",
    "Михайлович", "Богданович", "Ігорович", "Андрійович", "Тарасович",
    "Юрійович", "Дмитрович", "Олегович", "Степанович", "Васильович",
    "Євгенович", "Миколайович", "Романович", "Артурович", "Леонідович"
]

female_middle_names = [
    "Іванівна", "Петрівна", "Сергіївна", "Олександрівна", "Володимирівна",
    "Михайлівна", "Богданівна", "Ігорівна", "Андріївна", "Тарасівна",
    "Юріївна", "Дмитрівна", "Олегівна", "Степанівна", "Василівна",
    "Євгенівна", "Миколаївна", "Романівна", "Артурівна", "Леонідівна"
]

# Параметри
total_records = 500
male_count = int(total_records * 0.6)
female_count = total_records - male_count

data = []

# Функція генерації дати народження
def random_birthdate():
    return fake.date_of_birth(minimum_age=17, maximum_age=87).strftime("%d.%m.%Y")

# Генерація чоловічих записів
for _ in range(male_count):
    data.append([
        fake.last_name_male(),
        fake.first_name_male(),
        random.choice(male_middle_names),
        "Чоловіча",
        random_birthdate(),
        fake.job(),
        fake.city_name(),
        fake.address().replace("\n", ", "),
        fake.phone_number(),
        fake.email()
    ])

# Генерація жіночих записів
for _ in range(female_count):
    data.append([
        fake.last_name_female(),
        fake.first_name_female(),
        random.choice(female_middle_names),
        "Жіноча",
        random_birthdate(),
        fake.job(),
        fake.city_name(),
        fake.address().replace("\n", ", "),
        fake.phone_number(),
        fake.email()
    ])

# Перемішуємо усі записи
random.shuffle(data)

# --- Шлях до файлу ---
file_path = os.path.join("Lab6", "people_data.csv")

# --- Запис у CSV ---
with open(file_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow([
        "Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
        "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"
    ])
    writer.writerows(data)

print(f"CSV-файл успішно створено: {file_path}")
print(f"Кількість записів: {len(data)}")

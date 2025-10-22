import csv
from datetime import datetime, date
from openpyxl import Workbook
import os

# Шляхи до файлів
csv_filename = "Lab6/people_data.csv"
xlsx_filename = "Lab6/people_sort.xlsx"

def calculate_age(birthdate_str):
    """Обчислює повні роки з дати народження формату DD.MM.YYYY"""
    try:
        birthdate = datetime.strptime(birthdate_str.strip(), "%d.%m.%Y").date()
    except ValueError:
        return None
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

try:
    if not os.path.exists(csv_filename):
        print(f"Помилка: файл CSV '{csv_filename}' не знайдено або неможливо відкрити.")
        exit(1)

    with open(csv_filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)
except Exception as e:
    print(f"Помилка при відкритті CSV файлу: {e}")
    exit(1)

try:
    wb = Workbook()
    ws_all = wb.active
    ws_all.title = "all"

    sheet_names = ["younger_18", "18-45", "45-70", "older_70"]
    sheets = {name: wb.create_sheet(title=name) for name in sheet_names}

    headers_age = ["№", "Прізвище", "Ім'я", "По батькові", "Дата народження", "Вік"]

    # Аркуш "all"
    if rows:
        ws_all.append([str(h).strip() for h in rows[0].keys()])
        for row in rows:
            ws_all.append([str(v).strip() for v in row.values()])

    # Категорії за віком
    categories = {
        "younger_18": [],
        "18-45": [],
        "45-70": [],
        "older_70": []
    }

    for idx, row in enumerate(rows, start=1):
        birth_str = row.get("Дата народження", "").strip()
        age = calculate_age(birth_str)
        if age is None:
            continue
        row_data = [
            idx,
            row.get("Прізвище", "").strip(),
            row.get("Ім’я", "").strip(),
            row.get("По батькові", "").strip(),
            birth_str,
            age
        ]
        if age < 18:
            categories["younger_18"].append(row_data)
        elif 18 <= age <= 45:
            categories["18-45"].append(row_data)
        elif 46 <= age <= 70:
            categories["45-70"].append(row_data)
        else:
            categories["older_70"].append(row_data)

    # Запис у відповідні аркуші
    for sheet_name, data in categories.items():
        ws = sheets[sheet_name]
        ws.append(headers_age)
        for row in data:
            ws.append([str(v) for v in row])

    wb.save(xlsx_filename)
    print("Ok")
except Exception as e:
    print(f"Помилка при створенні XLSX файлу: {e}")

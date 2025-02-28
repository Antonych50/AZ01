import csv

with open("hh.csv", mode='r', encoding='utf-8') as file:
    # Создаём объект reader для чтения CSV
    reader = csv.reader(file)
    # Выводим содержимое файла построчно
    for row in reader:
        print(row)
import sqlite3
import csv
import codecs

conn = sqlite3.connect('db/test.db')
conn.text_factory = str
curr = conn.cursor()
curr.execute('''SELECT * FROM test''')

with codecs.open('отчет.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    # записываем заголовки столбцов
    writer.writerow([description[0] for description in curr.description])
    # записываем все строки
    writer.writerows(curr.fetchall())
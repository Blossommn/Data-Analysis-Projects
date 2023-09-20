import csv
import gspread
import time

MONTH = 'september'

file = f"BoA_{MONTH}.csv"

transactions = []

PAYMENT_NAMES = {"INTERNET PAYMENT - THANK YOU"}

def hsbcFin(file, PAYMENT_NAMES):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[1]
            amount = float(row[2])
            category = 'other'
            transaction = ((date, name, amount,category))
            print(transaction)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = hsbcFin(file, PAYMENT_NAMES)

for row in rows:
    wks.insert_row([row[0], row[1],row[3],row[2]],8)
    time.sleep(2)

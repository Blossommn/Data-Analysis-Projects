import gspread

gc = gspread.service_account()

sh = gc.open("Personal Finances")

print(sh.sheet1.get('A1'))
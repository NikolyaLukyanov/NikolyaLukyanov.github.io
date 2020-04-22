import pandas as pd

tables = pd.read_html("https://www.cbr.ru/currency_base/daily/",header=0, parse_dates=["Курс"])

print(tables)
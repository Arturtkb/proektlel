
import requests

class perevod:
    def __init__(self):
        self.rates = {}

    def get_rates(self):
        iz = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

        data = iz.json()

        for item in data:
            self.rates[item['cc']] = item['rate']

    def convert(self, amount, from_currency, to_currency):
        amount = float(input("Введіть число"))
        to_currency != "USD"
        chislo = amount / self.rates[to_currency]
        print(chislo)

perevod()




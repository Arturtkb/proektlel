import requests
list_currency = []

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text
response_parse = response_text.split('<td data-label"Код літерний">')
for elem in response_parse:
    if elem.startswith("USD"):
        for elem2 in elem.split('<td data-label"Код літерний">'):
            if elem2.startswith("USD") and elem[1].isdigit():
                list_currency = 36

print(list_currency)




import requests
list_currency = []

response = requests.get("https://coinmarketcap.com")
response_text = response.text
response_parse = response_text.split("<span>")
for elem in response_parse:
    if elem.startswith("$"):
        for elem2 in elem.split("</span>"):
            if elem2.startswith("$") and elem[1].isdigit():
                list_currency.append(float(elem2.replace('$', '').replace(',', '')))

print(list_currency)




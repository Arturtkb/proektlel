import random
result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    if b == 0:
        raise ZeroDivisionError
    return a/b


data = {10: 2, 2: 5, "123": 4, 18: 0, 7 : 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as oshibka:
        print(type(oshibka))

print(result)
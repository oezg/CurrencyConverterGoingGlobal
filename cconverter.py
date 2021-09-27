import requests
import json

currency = input()

url = "http://www.floatrates.com/daily/" + currency + ".json"
r = requests.get(url)
currency_dict = json.loads(r.text)

cache = {}
if currency.lower() == "usd":
    cache.update(eur=currency_dict["eur"]["rate"])
elif currency.lower() == "eur":
    cache.update(usd=currency_dict["usd"]["rate"])
else:
    cache.update(eur=currency_dict["eur"]["rate"])
    cache.update(usd=currency_dict["usd"]["rate"])


while True:
    currency2 = input()
    if not currency2:
        break
    amount = float(input())
    print("Checking the cache...")
    if currency2 in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache.update({currency2: currency_dict[currency2]["rate"]})
    conversion = round(amount * cache[currency2], 2)
    print(f"You received {conversion} {currency2.upper()}.")

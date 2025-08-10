def convert_currency(amount, from_currency, to_currency):
    rates = {"USD": 1.0, "EUR": 0.85, "RUB": 73.5}
    if from_currency not in rates or to_currency not in rates:
        return "Неподдерживаемая валюта!"
    amount_in_usd = amount / rates[from_currency]
    return amount_in_usd * rates[to_currency]

try:
    amount = float(input("Введите сумму: "))
    from_curr = input("Из валюты (USD, EUR, RUB): ").upper()
    to_curr = input("В валюту (USD, EUR, RUB): ").upper()
    result = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
except ValueError:
    print("Введите корректную сумму!")
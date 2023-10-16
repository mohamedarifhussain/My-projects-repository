import requests
import re
print("Welcome to currency converter")

x = requests.get(url='https://www.bookmyforex.com/blog/world-currencies-indian-currency-exchange-rate/')
datas = x.text
converter_is_on = True


# with open(r"C:\Users\USER\Documents\Python Scripts\project_7_currency_converter\currency_data.txt", "w+",
#           encoding="utf-8") as f:
#     f.writelines(datas)

currency_list = datas.splitlines(keepends=True)[1745:2372]

# print(currency_list)


def currency_finder(country):
    for i in currency_list:
        if country.lower() in i.lower():
            index = currency_list.index(i)
            currency_item = currency_list[index+3]
            currency = re.search(r"[0-9]*\.?[0-9]+", currency_item)
            if currency:
                currency_index = currency.span()
            else:
                return "There is no currency like that."
            currency_rate = float(currency_item[currency_index[0]:currency_index[1]+1])
            return currency_rate
    return "There is no currency like that."


while converter_is_on:
    country_name = input("\nEnter the country name 1: ")
    money = float(input('Enter the money: '))
    country_name2 = input("Enter the country name 2: ")
    print(f"\n{country_name}: {money}")
    money_1 = currency_finder(country_name) * money
    money_2 = money_1/currency_finder(country_name2)
    print(f"{country_name2}: {money_2}")
    choice = input("\nDo you want to check the rate again(yes/no): ")
    converter_is_on = True if choice == 'yes' else False

print("\nCurrency converter turned off.")

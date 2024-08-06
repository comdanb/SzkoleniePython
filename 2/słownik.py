dictionary = dict()
dictionary['kot'] = 'cat'
dictionary['pies'] = 'dog'
dictionary['mysz'] = 'mouse'
print(dictionary.keys())
print(dictionary.values())
slowo = input("podaj zwierze: ")
print(slowo)
slowo = slowo.lower().replace(" ", "")
print(slowo)
print("Tłumaczenie", slowo, "na angielski to:", dictionary[slowo])

# TestGIT
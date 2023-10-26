"""

    Sorting techniques.

"""
sa_countries = [
    ('Brazil', 204000000), ('Columbia', 48500000),
    ('Argentina', 43100000), ('Peru', 31100000)
]

print('The starting data structure:')
print(sa_countries)

print('\nin-place sort:')
sa_countries.sort()
print(sa_countries)


print('\ncreating a new list by using sorted():')
new_countries = sorted(sa_countries)
print(new_countries)


print('\nsorting in reverse (works for both sort() and sorted() ):')
sa_countries.sort(reverse=True)
new_countries = sorted(sa_countries, reverse=True)
print(sa_countries)
print(new_countries)

print('\ngetting a reverse-iterator:')
for i in reversed(range(10)):
    print(i, end=' ')
else:
    print()


print('\nsort() using a key:')
def sort_by_population(country):
    return country[1]


x = sort_by_population(('my name', '2023'))
y = sort_by_population

z = y(('my name', 2023))
print(z)

print(type(x), type(y))



sa_countries.sort(key=y)
print(sa_countries)


print('\nsorted() using a key:')
new_countries = sorted(sa_countries, key=sort_by_population, reverse=True)
print(new_countries)


print('\nsorting records using a key and lambda:')
sa_countries.sort(key=lambda country: country[1], reverse=True)
print(sa_countries)

# TODO: używać ctrl+alt+L -  w celu zachowania zgodności z PEP-8

liczby = [5, 2, 1, 4, 3]

print(liczby)

indeks_min = None
indeks_max = None

for index in range(len(liczby)):
    if index == 0:
        indeks_max = index
        indeks_min = index
    else:
        if liczby[index] > liczby[indeks_max]:
            indeks_max = index
        if liczby[index] < liczby[indeks_min]:
            indeks_min = index

print(indeks_min, indeks_max)
print("")
# nie stosujemy nazw zmiennych takich jak słowa kluczowe w pythonie
# warto poszukać słów kluczowych w pythonie
# hint: w pycharmie może się podświetlać na niebiesko
# TODO: Poczytać
min_ = liczby[indeks_min]
max_ = liczby[indeks_max]

liczby[indeks_max] = min_
liczby[indeks_min] = max_

print(liczby)

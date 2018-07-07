# Tupla lub krotka to struktura, która przechowuje więcej niż 1 wartość na raz
# krotki nie służą do modyfikacji

zmienna = (1,2,3,4)
print(zmienna)

a = ('ala', 'ma', 'kota')
b = ('ala','ma', 3.5 , 'koty', 5,6,7,8)

print(a,b)
print(len(a))   # ile masz elementów
print(a[0])

# wypisz wszystkie elementy tupli b
print('================')
i = 0
while i < len(b):
    print(b[i])
    i+=1
print('================')

print(b)
print(b[1:3])
print(b[1:])
print(b[:3])
print(b[1:6:2])
print(b[::2])
print(b[:-1])
print(b[-3:])
print(b[1:-1])
print(b[::-1])
print(b[5:2])
print(b[5:2:-1])
print(b[2:5:-1])
print(b[-1])

print(b + ('to','jest','nowa','tupla'))
# lista to struktura podobna do krotki, ale mogę ją modyfikować

lista = [1,2,3,4,5,6,7,1,2,3,1,1,1]

print(sum(lista))

print(len(lista))
print(lista[0])
print(lista[-1])
print(lista[::2])

lista.append('ala')
print(lista)

lista.insert(3,'kot')
print(lista)

lista.insert(100,'tu byłem Tony Halik')
print(lista)

print(lista.count(1))

lista[3] = 'tu był element czwarty'
print(lista)

lista[3:7] = [0,0,0,0,0,0,0,0,0]
print(lista)


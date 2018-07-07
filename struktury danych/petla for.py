lista = [1,2,3,4,5,6,7,8]

for element in lista:
    print(element)

tupla = ('ala','ma',3,'koty','które','ją','nienawidzą')

print('======= po prostu for ===========')
for el in tupla:
    print(el)

print('======= enumerate ===========')
for nr, element in enumerate(tupla):
    print(nr, element)

print('======= range(10) ===========')
for i in range(10):
    print(i, end=' ')

print('======= range(len(tupla) ===========')
for i in range(len(tupla)):
    print(i,tupla[i])

print('======= range(1,len(tupla),2) ===========')
for i in range(1,len(tupla),2):
    print(i, tupla[i])

print('======= cuda na kiju ===========')
kopia = tupla[-1::-1]
for el in kopia:
    print(el)
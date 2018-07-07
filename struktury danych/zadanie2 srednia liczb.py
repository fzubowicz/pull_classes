zestaw = []

liczba = input('podaj liczbę: ')
while liczba != '' and len(zestaw) < 10:
    zestaw.append(int(liczba))
    liczba = input('podaj liczbę: ')

print(f'średnia to {sum(zestaw)/len(zestaw)}')
      
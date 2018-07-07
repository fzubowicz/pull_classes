# Napisz program wypisujacy wszystkie libczy od 0 do 100, podzielne
# przez 3 lub podzielne przez 5. Wypisz takze jak duzo takich liczb
# wystapiło w tym przedziale.

licznik = 0
for liczba in range(101):
    if (liczba % 3 == 0) or (liczba % 5 == 0):
        print(liczba)
        licznik += 1

print(f'w zakresie 0-100 jest {licznik} liczb podzielnych przez 3 lub 5')
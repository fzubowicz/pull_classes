#text = input("Podaj tekst: ")
text = "Ala <ma> kota <psotka>"
text = "<><>"
# ver 1 - najprostsza - napis tylko raz zawiera  <>

start = text.index('<')+1
stop = text.index('>')

print(stop - start)

start = text.find('<')+1
stop = text.find('>')

print(stop - start)

czy_jest_miedzy_nawiasami = False
liczba_znakow_miedzy_nawiasami = 0

for znak in text:
    if znak == '<':
        czy_jest_miedzy_nawiasami = True
    elif znak == '>':
        czy_jest_miedzy_nawiasami = False
    elif czy_jest_miedzy_nawiasami:
        liczba_znakow_miedzy_nawiasami += 1

print(liczba_znakow_miedzy_nawiasami)

# ver 2 - <> moga się pojawiac wiele razy


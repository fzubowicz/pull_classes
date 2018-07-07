text = input("Podaj napis: ")

SAMOGLOSKI = "aeiouy"
             # ['a', 'e']

ile_samoglosek = 0

# for znak in text:
#     if znak.lower() in SAMOGLOSKI:
#         ile_samoglosek += 1

for s in SAMOGLOSKI:
    x = text.lower().count(s)
    print(f"{s} występuje: {x}")
    ile_samoglosek += x


print(f"Znaleziono {ile_samoglosek} samogłosek")




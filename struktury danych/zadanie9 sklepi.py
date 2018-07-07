produkty = {
    'ziemniaki': 1.99,
    'cebula': 1.29,
    'kapusta': 3.20,
    'pomidory': 8.0
}

print("W naszym sklepie dostępne są następujące produkty ")

for k, v in produkty.items():
    print(f"- {k} w cenie: {v}")

produkt = input("Zachęcamy do zakupów. Co podać? [Wpisz: end by zakończyc zakupy] ")
ile = float(input(f"Ile kg {produkt} podać? "))

koszt_10 = ile * produkty[produkt]
koszt1 = ile * produkty[produkt]

print(f"Proszę o: {koszt_10} PLN")

print(globals())

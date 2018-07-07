# tworzymy napis i przypisjemy go do zmiennej
napis = "Ala ma kota"

# możemy sprawdzi jakie metody są dostepne dla tego typu:
print(dir(napis))

# w konsoli po prostu dir(napis)

# 'capitalize',
print(napis.capitalize(), " | capitalize")

# 'casefold',
print(napis.casefold(), " | casefold")

# 'center',
napis2 = napis+" | center"
print(napis2.center(80))

# 'count',
print(napis.count("a"), " | count")

# 'encode',
print("Zażółć gęślą jaźń".encode(), " | encode")

# 'endswith',
# 'expandtabs',
# 'find',
print(napis.find("a "), " | find")

# 'format',
print("To jest {} {} {}".format("napis", "a", "b"), " | format")

# 'format_map',
# 'index',
# 'isalnum',
# 'isalpha',
# 'isdecimal',
# 'isdigit',
a = "1"
b = "   10 "
c = "cos"
d = "10  "

print("is digit check")
print(a.isdigit(), b.isdigit(), c.isdigit(), d.isdigit())
print( b.strip().isdigit(), d.rstrip().isdigit())
           #"10".isdigit()

b = "10a"
if b.isdigit():
    c = int(b)

# 'isidentifier',
# 'islower',
# 'isnumeric',
# 'isprintable',
# 'isspace',
# 'istitle',
# 'isupper',
# 'join',
# 'ljust',
# 'lower',

print(napis.lower(), " | lower")

# 'lstrip',

wielelinijek = """
To jest
wieloliniow
napis
"""
wielelinijek2 = "To jest\nwieloliniow\nnapis"
wielelinijek2 = r"To jest\nwieloliniow\nnapis"
wielelinijek3 = "To jest\\nwieloliniow\\nnapis"

print(wielelinijek)
print(wielelinijek2)
print(wielelinijek3)

brands = ["fenti", "Haus Labs", "rare beauty", "rem beauty", "huda beauty", "Tarte"]
x = len(brands)
print (len(brands))
for x in brands:
    print(x)
novy= input("zdejte novou znacku")
brands.append(novy)
print(len(brands))
brands.pop(4)
brands.sort()
brands.reverse()
for x in brands:
    print(x)





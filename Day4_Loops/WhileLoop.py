# tekrarlanan islemler icin kullaniliyor

# 10'a kadar olan sayilari yaz
i = 0

while i<10:
    print(i)
    i += 1

# Ust limiti kullanicinin belirledigi bir sayiya kadar yaz

i = 1
ustlimit = int(input("Ust limiti giriniz"))

while i<ustlimit:
 print(i)
 i += 2

i = 1
ustlimit = int(input("Ust limiti giriniz"))

while i<ustlimit:

    i += 1
    if i == 30:
        break
    print(i)

i = 1
ustlimit = int(input("Ust limiti giriniz"))

while i<ustlimit:

    i += 1
    if i == 30:
        continue
    print(i)

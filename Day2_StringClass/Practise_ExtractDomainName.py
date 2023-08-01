
# Verilen emailden domain ismini cikartan programi yaziniz:

email = "fatih@istanbul.com"

# email variable ini slice etmemiz lazim:
# email[baslangic(@ isaretinin oldugu index):bitis( . noktanin oldugu index)]

ind1 = email.find("@")
ind2 = email.find(".")
print(email[ind1])
print(email[ind2])

print(email[ind1+1:ind2])

print("TLD domain extension")
print(email[ind2:len(email)])

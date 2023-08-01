# string is immutable
# degistirmek icin re-assign yapmak gerekir
strHello = "Hello IsTanBul!"

# strHello object olusturdu
# bu object String class'dan olustu

# index
index = strHello[10]
print(index)
print(strHello[-1])

# slicing
print(strHello[:-1])
print(strHello[-1:])
print(strHello[:3])

print(strHello[::-1]) # reversing
print(strHello[1:15:3]) # reversing
print(input("What's in your mind?")[::-1]) # reversing

ind_char = strHello.index("l")
ind_char2 = strHello.index("l", 4, 51)
print(ind_char)
print(ind_char2)

# len()
length = len(strHello)
print(length)

# lowercase: lower()

print(strHello.lower())

# upprcase: upper()

print(strHello.upper())

strHello = strHello.upper()
print(strHello)

# capitalize()
strHello = strHello.capitalize()
print(strHello)

# title()
strHello = strHello.title()
print(strHello)

# replace()

strHello = strHello.replace(" ","_")
strHello = strHello.replace("o","O")
strHello = strHello.replace("l","L")
print(strHello)

# startswith()

print(strHello.startswith("H"))
print(strHello.startswith("O"))

# endswith()

print(strHello.endswith("!"))
print(strHello.endswith("L"))

# find()
print('ilk L harfi index numarasi: ',strHello.find("L")) # index numarasini veriyor
print('ilk l harfi index numarasi: ',strHello.find("l")) # index numarasini veriyor. eger yoksa -1 verir

# count()
print('L harfi sayisi: ',strHello.count("L")) # tekrar eden l harf sayisi veriyor
print('el harfi sayisi: ',strHello.count("el")) # tekrar eden l harf sayisi veriyor
print('eL harfi sayisi: ',strHello.count("eL")) # tekrar eden eL kelimesi sayisi veriyor

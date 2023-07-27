number1 = input("Enter a number 1:")
number2 = input("Enter a number 2:")

total1 = number1 + number2 # text concat
total2 = int(number1) + int(number2) # addition
bolum = int(number1) / int(number2) # division - converts to float
bolumInt = round(bolum) # division - converts to float

print(total1)
print(total2)
print(bolum)
print(bolumInt)

strTotal = "iki sayinin toplami: " + str(total2)
print("iki sayinin toplami:", total2)
print(strTotal)

print(type(strTotal))

floatTotal = float(total2)
print(type(floatTotal))

boolAnswer = True
boolAnswer2 = False

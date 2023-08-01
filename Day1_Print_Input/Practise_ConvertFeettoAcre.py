# Exercise 4: Area of a Field
# Create a program that reads the length and width of a farmer's field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

sqft = int(input("Arazinin sq feet degerini girin"))

acre = sqft / 43560
print("Acre degeri=",acre)

donum = acre * 4.04686
print("Donum degeri=",donum)

metrekare = donum * 1000
print("Metre Kare degeri=",metrekare)

mile = int(input("Mesafenin mile degerini girin:"))
km = mile * 1.65
print("KiliMetre degeri=", km)

'''
Exercise 37: Name that Shape
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
'''

sides = int(input("Kenar sayisi giriniz"))

if sides == 3:
    print("Ucgen")
elif sides == 4:
    print("Dortgen")
elif sides == 5:
    print("Besgen")
elif sides == 6:
    print("Altigen")
else:
    print("Lutfen 3 ile 6 arasinda bir rakam giriniz")

'''
Exercise 38: Month Name to Number of Days
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display "28 or 29 days"
for February so that leap years are addressed.
'''

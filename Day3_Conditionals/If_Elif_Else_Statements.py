# program flow
bool_a = False
bool_a = 5==3
bool_a = 5!=3 # True
bool_a = 5==5
bool_a = 5>2
bool_a = 5<2
bool_a = 5<=5
bool_a = 5>=5
if bool_a:
    print("Hello")
intTemp = 95
if intTemp >= 30 and intTemp<40:
    print("Hava sicak")
if intTemp>=40 and intTemp<50:
    print("Hava cok asiri sicak")
if intTemp>=50:
    print("Acil durum, disari cikmayin")

num = 221

if num % 2 == 0:
    print(num,"cift sayidir")
else:
    print(num,"tek sayidir")

if num % 2 == 0:
    print(num,"cift sayidir")
elif num % 2 == 1:
    print(num,"tek sayidir")

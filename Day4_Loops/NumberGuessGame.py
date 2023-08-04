computerNumber = 2

#userNumber = int(input("Numarani gir"))

# numarayi bilirse
while True:
    userNumber = int(input("Numarani gir (1-50 arasi)"))

    if computerNumber == userNumber:
        print("Numarayi bildin!")
        break

    else: # numarayi bilemezse

        # computerNumber userNumber dan buyukse daha kucuk gir yazacak
        if computerNumber > userNumber:
            print("bilemedin, daha buyuk rakam dene!")

        # computerNumber userNumber dan kucukse daha buyuk gir yazacak
        else:
            print("bilemedin, daha kucuk rakam dene!")

from forex_python.converter import CurrencyRates
c = CurrencyRates() # object olusturuyor
amount = int(input("Kac dolarin var?"))

TL = c.get_rate('USD', 'TRY')
EU = 0.91
Pound = c.get_rate('USD', 'GBP')
KuwaitDinar = 0.31
Yuan = 7.14

print(amount, "Dolar", amount * TL, "TL eder")
print(amount, "Dolar", amount * EU, "Euro eder")
print(amount, "Dolar", amount * Pound, "Sterlin eder")
print(amount, "Dolar", amount * KuwaitDinar, "Kuveyt Dinari eder")
print(amount, "Dolar", amount * Yuan, "Yuan eder")

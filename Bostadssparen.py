#Version 1.0 Oscar Wissén:
#Skapnde av kod. Sätta variabler och felhantering av dessa. 2018-07-29.


import math
import numpy
import tkinter
import sys


#Skapa en variabelsinläsningsfunktion som innehåller felhantering:
def variblereader(Variable, minvalue, text_for_var):

#Gör ett antagande om att personen ej har bostadslån om personen ej har en lägenhet
    if Variable == "Skuld" and Lagenhet == float(0):
        Skuld = float(0)
        print("Eftersom du är utan bostad antar vi att är skuldfri")
        return Variable
    Variable=float(input(text_for_var))
#Skapa felhanteringen
    while Variable<minvalue:
        print(Variable, "Är ej ett godkänt värde, vänligen försök igen")
        Variable = float(input(text_for_error))
    print(Variable)
    return(Variable)


#Deklarera variabler
Lagenhet=variblereader("Lagenhet",0,"Skriv in värdet på din nuvarande bostad, du ej äger någon skriv in värdet 0: ")
Skuld=variblereader("Skuld",0,"Skriv in bostadslånet på din nuvarande bostad, du ej äger någon skriv in värdet 0: ")
Sparande=variblereader("Spar",0, "Skriv in ditt sedan tidigare sparade kapital: ")
ManSpar=variblereader("Sparande", 0,"Skriv in hur mycket du sparar varje månad: ")
Ranta=variblereader("Interest",-math.inf, "Skriv in marknadsräntan :")

test=Lagenhet+Skuld
print(test)

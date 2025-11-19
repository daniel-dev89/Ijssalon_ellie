from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    
    kortingsprijs = prijs * 1 - korting
    tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro"
    return tekst

print(aanbieding_1("aardbei", 4, (0.4)))

def inkomsten_totaal(inkomsten, btw):
    
    totaal_exl= sum(inkomsten)
    totaal_incl = totaal_exl * (1 + btw) # 9.0 % btw
    return totaal_incl

weekinkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
totaal = inkomsten_totaal(weekinkomsten, btw)

tekst = f"Het totaal van alle inkomsten van deze week is {totaal:.2f}, waarover {btw * 100:.0f} % btw betaald dient te worden" 

print(tekst)

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return (laagste, hoogste)

inkomsten = [220, 430, 125, 160, 205, 90, 235]
resultaat = laag_en_hoog(inkomsten)

print(resultaat)

def gemiddelde(mijn_lijst):
#bereken het gemiddelde 
    gemiddelde =  sum(mijn_lijst) / len(mijn_lijst)

    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} , euro"

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(mijn_lijst))

#functie die laag_hoog gebruikt

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst = [10,5,3,2,1,2,9]
resultaat = meervoudig(invoer_lijst)
print(resultaat)

#functie die laag_hoog aanroept en korte_lijst teruggeeft
def combinatie(invoer_lijst_2):
   
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return resultaat

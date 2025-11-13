# Aufgabe: eine liste aus zahlen, ein wert der aus der kombination 2er zaheln aus der liste entsteht.
# 2 Funktionen die einmal die möglichkeiten zählen, einmal die möglichkeiten zurück geben


listn = [5,6,5,7,9,5,1,6,12,8,2,10,9,11,12,3]
wanted = 12

def combinations(listn, sum):
    setsl= set()
    for i in range(len(listn)-1):
        for m in listn[i:]:
            if listn[i] + m == sum:
                setsl.add(tuple(sorted([listn[i], m]))) # damit (5,7) und (7,5) nicht doppelt gezählt werden (Idee von KI mit sortieren)
    return len(setsl), setsl


count, liste = combinations(listn, wanted)
print(f"Anzahl der Kombinationen: {count}")
print("Kombinationen:")
print (liste)
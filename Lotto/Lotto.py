import random as rnd

anzahl_zahlen = 45

def main():
    lottozahlen = []
    lottozahlen = auffuellen(lottozahlen)
    print (lottozahlen)
    zeihung = ziehung(lottozahlen)
    print (zeihung[anzahl_zahlen-6:anzahl_zahlen])

def auffuellen(lottozahlen):
    lottozahlen= []
    for i in range(1, anzahl_zahlen+1):
        lottozahlen.append(i)
    return lottozahlen

def ziehung(lottozahlen):
    for i in range(6):
        ziehung = rnd.randint(0,anzahl_zahlen-1)
        zahl = lottozahlen[anzahl_zahlen-1-i]
        lottozahlen [anzahl_zahlen-1-i]= lottozahlen[ziehung]
        lottozahlen [ziehung]= zahl
    print (lottozahlen)
    return lottozahlen

if __name__ == "__main__":
    main()
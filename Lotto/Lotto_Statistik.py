import random

values = 45

def main():
    print("Lotto Statistik")
    draws = input("Anzahl der Ziehungen: [default: 1000] ")
    try :
        if int(draws) <= 0:
            draws = 1000
    except ValueError:
        draws = 1000
    draws = int(draws)
    statistic = { i:0 for i in range(1, values+1) }
    for i in range (1, draws + 1):
        draw = random.randint(1,values)
        statistic[draw] += 1
    print (statistic)

if __name__ == "__main__":
    main()
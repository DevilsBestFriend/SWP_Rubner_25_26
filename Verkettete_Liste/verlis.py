import classes
    


def main():
    listn = classes.LinkedList(1)
    
    listn.apendieren(2)
    listn.apendieren(3)
    listn.apendieren("test")
    
    x = 0
    for l in listn:
        print(l)
        x += 1
        if x >= 10:
            continue
        
    
    print(listn.first)
    print(listn.last())
    print(listn.all())
    
 
if __name__ == "__main__":
    main()
    
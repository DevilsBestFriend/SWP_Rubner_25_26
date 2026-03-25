import classes
    


def main():
    listn = classes.LinkedList(1)
    
    listn.__add__(2)
    listn.__add__(3)
    listn.__add__("test")
    
    for l in listn:
        print(l)
    print("")
    
    listn.insertieren(1, "insert")
    listn.deletieren(3)
    
    print("last= ", listn.last())
    print("first= ", listn.first())
    print("last= ", listn.last())
    print("all=", listn.all())
    print("pop=", listn.pop())
    print("all= ", listn.all())
    
 
if __name__ == "__main__":
    main()
    
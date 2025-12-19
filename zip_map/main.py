if __name__ == "__main__":
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]
    ziped_types = list(zip(names,ages,scores))
    print(ziped_types)

    print("\n")

    filtered_items = list(filter(lambda input: input[1] >= 18 and input[2] >= 80, ziped_types))
    print(filtered_items)

    print("\n")

    maped_items = list(map(lambda input: dict({"name":input[0],"age":input[1],"score":input[2]}), ziped_types))
    print(maped_items)
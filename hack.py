for i in range(101):
    print("{}{}{}".format(
        "Rock" if i % 3 == 0 else "",
        "&" if (i % 3 == 0) and (i % 5 == 0) else "",
        "Roll" if i % 5 == 0 else "",
    ) or i)

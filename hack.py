for i in range(101):
    if i % 5 == 0 and i % 3 ==0:
        print("Rock&Roll")
    elif i % 3 == 0:
        print("Rock")
    elif i % 5 == 0:
        print("Roll")
    else:
        print(i)



print("\n\n\n\n")
[ print("Rock&Roll") if i % 5 == 0 else print(i) for i in range(101) ]
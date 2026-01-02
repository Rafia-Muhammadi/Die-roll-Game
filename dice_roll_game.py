import random
while (True):
    start=input("Roll the dice? (y/n):").lower()
    if(start == 'y' or start ==' Y'):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        print(f"({num1},{num2})")
    elif(start == 'n'):
        print("Thank For Playing")
    else:
        print("Invalid Choice!")



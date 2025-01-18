positive_integer = int(input("Enter a positive integer:"))
def factors():
    for i in range(1,positive_integer+1):
        if positive_integer%i == 0:
            print(f"{i} is a factor of {positive_integer}")
factors()

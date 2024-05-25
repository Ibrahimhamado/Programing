def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
number=int(input("Enter an integer number and greater than 0:"))
if number<0:
    print("Error,type eroor negativ number")
else:
    print("Factorial of", number,"is", factorial(number))
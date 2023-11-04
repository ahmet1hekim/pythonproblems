def factorial(number):
    if(number!=1):
        return number*factorial(number-1)
    else:
        return number
print(factorial(int(input("sayi\n"))))    
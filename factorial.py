def fact(n): 
    product = n #assigning product inital value
    while(n != 1): 
        product = product*(n-1) #multiplying with previous number untill n=1
        n = n-1
    return product

try:
    number = int(input("Enter the number"))
    print(fact(number))    #calling the function
except ValueError:
    print("Enter an integer")

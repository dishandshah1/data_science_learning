
#Using For Loop

number = input("Enter the number")

#product = int(number)
#for i in range((int(number) - 1),0,-1):
#    product = product*i
    
#print(product)



#using while loop

n = int(number)
product = int(number)
while(n != 1):
    product = product*(n-1)
    n = n-1

print(product)
    
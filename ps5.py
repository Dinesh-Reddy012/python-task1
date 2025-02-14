# num1 = int(input("enter lower bound"))
# num2 = int(input("enter upper bound"))

# for p in range(num1,num2+1):
#     count = 0
#     for i in range(1,p+1):
#        if p % i == 0:
#            count+=1


#     if count == 2:
#         print(p,"is prime")
#     else:
#         print(p,"not a prime")

#for 1st prime num after given num
num= int(input("enter a number"))
# while True:
#     num += 1
#     count = 0
#     for i in range(1,num + 1):
#         if num % i ==0:
#            count +=1

#     if count == 2:
#          print(num)
#          break
    
#for 1st prime num below given num
while num>0:
    if num<2:
        print("enter number above 2")
        break
    num -= 1
    count = 0
    for i in range(1,num+1):
        if num % i ==0:
           count +=1

    if count == 2:
         print(num)
         break


# for first nearest prime above or below    

    num += 1
    count = 0
    for i in range(1,num + 1):
        if num % i ==0:
           count +=1

    if count == 2:
         print(num)
         break

    if num<2:
        print("enter number above 2")
        break
    num -= 1
    count = 0
    for i in range(1,num+1):
        if num % i ==0:
           count +=1

    if count == 2:
         print(num)
         break
     
    
    


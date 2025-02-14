#febnocci series
# num= int(input("Enter number of fib needed"))
# #0 1 1 2 3 5 8 13

# #step1 - intialize bases
# n1 = 0
# n2 = 1


# print(n1)
# print(n2)


# for i in range(0,num-2): #for range 5 range(0,num-2) ,-2 because n1 and n2 are already printing
#     temp = n1 + n2
#     n1 = n2 
#     n2 = temp
#     print(temp)

#Q2.Armstrong number?
# num1 = int(input("enter a number to check if its a armstrong number"))

# temp = num1

# sum = 0
# while temp > 0:
#     rem = temp % 10
#     print(rem)
#     sum += rem ** 3
#     temp = temp // 10
# print ("ArmStrong") if sum == num1 else print ("Not an Armstrong number")


#for any no of digits digits
# lower_range = 100
# upper_range = 999

# for i in range(lower_range,upper_range + 1):
#     temp = i
#     len_i = len(str(i))
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum += rem ** len_i
#         temp = temp // 10

#     if i == sum:
#          print(i, "Is Armstrong")


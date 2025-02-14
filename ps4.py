#reverse a number using a while loop
# num = 54321

# rev_num = 0
#sum = 0 # for sum of digits
# while num>0:
#     rem = num % 10
     #  sum += rem #will give sum of the digits 
#     rev_num = rev_num * 10 + rem
#     num = num // 10 

# print(rev_num)

#to check for a palindrome(for number)
# num = 121
# temp = num
# rev_num = 0

# while num>0:
#     rem = num % 10
#     rev_num = rev_num * 10 + rem
#     num = num // 10 

# print(rev_num)

# if temp == rev_num:
#     print("the given number is a palindrome")
# else :
#     print("the given n umber is not a palindrome")

#count the number of digits in a given number
# num1= 587648488
# temp = num1
# count=0
# while temp>0:
#     rem =  temp % 10
#     count += 1
#     temp = temp // 10

# print(count)

#Implement a basic login system where the user has three attempts to login

# user_name = "pushpa raj"
# user_pass = "srivalli"

# allowed_attempts = 3

# while allowed_attempts>0:
#     print(" enter user name and password")
#     print("you have",allowed_attempts,"to enter correct user credentials")

#     username_input = input("enter username")
#     password_input = input("enter your password")

#     if username_input == user_name and  password_input == user_pass :
#         print("you have logged in successfully")
#         break
#     else :
#         print("log in failed")
     
#     allowed_attempts -= 1


#find if a given number is prime
#method 1
# num2 = 3
# count = 0
# for i in range (1,num2 + 1):
#        if num2 % i == 0:
#               count+=1
    

# if count == 2:
#        print("given number is a prime number")

# else:
#        print("the given number is not a prime number")

#method 2
# num1=77
# flag = True
# if num1 == 2:
#     print("Is a prime")
# else:
#       for i in range(2,num1):
# #for i in range(2,int((num1)/2 + 1))   #takes less time
#          if num1 % i == 0:
#              flag = False
#              break

# print("Is a prime number") if flag == True else print("Not a prime number")



#method 3
# num1=13
# flag = True
# if num1 == 2:
#     print("Is a prime")
# else:
#     for i in range(2,int(num1 ** 0.5)+1):
#          if num1 % i == 0:
#              flag = False
#              break

# print("Is a prime number") if flag == True else print("Not a prime number")



#in a range primt prime numbers

num1=1
num2=100



for num in range(num1,num2+1):
    count = 0
    for j in range(1,num+1):
       if  num % j == 0:
           count +=1

    if count== 2:
        print(num,"is a prime number")

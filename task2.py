# Q1.A wizard gives you a magic number and asks you to guess if 
# it’s divisible by 3 and 5. If it is, print "FizzBuzz". 
# If it’s only divisible by 3, print "Fizz". If it’s only 
# divisible by 5, print "Buzz". Otherwise, print the number itself.
# input1 = float(input("enter a number"))
# if input1 % 3 == 0 and input1 % 5 == 0:
#     print("fizz buzz")
# elif input1 % 3 == 0:
#     print("Fizz")
# elif input1 % 5 == 0:
#     print("Buzz")
# else:
#     print("check whether you have enterd a number which is mutiple of 3 or 5")


# Q2.Write a Python program that checks 
# if three given sides form a valid triangle.
#  A triangle is valid if the sum of any two sides is greater than the third.
# s1=float(input("enter side1"))
# s2=float(input("enter side2"))
# s3=float(input("enter side2"))

# if (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1) :
#     if s1==s2==s3 :
#        print("equilateral triangle")
#     elif (s1==s2) or (s2==s3) or (s3==s1):
#         print("isossceles")
#     else:
#         print("all sides are different")5

# Q3.
# act_bal=5000
# withdrawn_amt = 5500
# print("transaction successful") if withdrawn_amt % 100 ==0 and withdrawn_amt<act_bal else print("amount must be multiple of 100 and withdrawal amt should not exceed acount bal")


# Q4.
w1_atck1 =55
w2_atck2 =66
w1_health =10
w2_health =15

if w1_atck1 > w2_atck2 :
    print("warrir1 wins")
elif w1_atck1 < w2_atck2 :
    print("warrior2 wins")
else :
    if w1_health > w2_health :
        print("warrior1 wins")
    elif w1_health < w2_health :
        print("warrior2 wins")
    else :
        print("Draw")
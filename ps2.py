# Q1.check for leap year

# year=int(input("Enter year"))

# 1st way:
# if (year % 100!=0 and year %4==0) or year % 400==0:
#     print("Leap year")
# else:
#     print("not a leap year")

# 2nd and best way
# print("leap year") if(year % 100!=0 and year %4==0) or ( year % 400==0) else print("not a leap year")

# Q2.chec
# side1 =float(input('side1'))
# side2 =float(input('side2'))
# side3 =float(input('side3'))

# s1+s2 > s3 ;s3 + s1> s2;s2+s3>s1
# print("Triangle possible") if (side1 + side2 > side3) and  (side3 + side1 > side2) and  (side2 + side3 > side1) else print("Triangle not possible")


# Q3.

str1 = input("enter a single character").lower()
if len(str1) >1 or len(str1)==0:
  print(" invalid input,give only single character")
else:
  if str1 in ['a','e','i','o','u'] :
    print("Vowel")
  elif str1.isalpha(): 
    print("consonant")
  else:
   print("neither")

# Q1. maximum number,minimum number in list and sum of list

# list =[1,2,7,8,9,4,14]
# max_num=list[0]
# min_num=list[0]
# sum =0
# for i in range(0,len(list)):
#     sum+=list[i]
#     if list[i]>max_num:
#         max_num=list[i]

#     if list[i]<min_num:
#         min_num=list[i]

# print(max_num)
# print(min_num)
# print(sum)


# Q2.print arthematic operations of two numbers using single function

# def  arthematic_op(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a**b)
#     print(a//b)

# arthematic_op(2,2)


# Q3.find oldest(greater age) among two persons
# suresh_age=25
# ramesh_age=28
# if suresh_age > ramesh_age:
#     print("suresh age is greater than ramesh age, which is :",suresh_age)
# elif suresh_age == ramesh_age:   #edge case (never miss it)
#     print("suresh and ramesh are of same age")
# else:
#     print("ramesh age is greater than suresh age,which is :",ramesh_age)


#*# (2nd way) in one line using terinary operator 
# str1="suresh is younger" if suresh_age < ramesh_age else "ramesh is younger"
# print(str1)


# Q3.find oldest and youngest among three persons
# suresh_age=int(input("enter suresh age"))
# ramesh_age=int(input("enter ramesh age"))
# dinesh_age=int(input("enter dinesh age"))

#my own
# if suresh_age>ramesh_age:
#     if suresh_age>dinesh_age:
#         print("suresh is elder among three")
#     else :
#         print("dinesh is elder among three")



# if ramesh_age > suresh_age:
#     if ramesh_age>dinesh_age:
#         print("ramesh is elder among three")
#     else:
#         print("dinesh is elder among three")


#2nd way(sir's)
# if ramesh_age < suresh_age and ramesh_age < dinesh_age :
#     print("ramesh is youngest")
# elif  suresh_age<dinesh_age :
#     print("suresh is youngest")
# else :
#     print("dinesh is youngest")

#*#3rd way using terinary operator

# str2= "ramesh is youngest" if ramesh_age<suresh_age and ramesh_age < dinesh_age else "suresh is youngest" if suresh_age<dinesh_age else "dinesh is youngest"


# actual_username = "Dj Tillu"
# actual_password = "Radhika"

# username_input = input("Enter user name")
# password_input = input("Enter password")


# if username_input == actual_username and password_input == actual_password:
#     print("Login succesful and you are tillu")
# elif username_input != actual_username and password_input != actual_password :
#     print("wrong username and password")
# elif username_input != actual_username:
#     print("Username is wrong")
# else:
#     print("Password ids wrong")
#     print("Login failed...")

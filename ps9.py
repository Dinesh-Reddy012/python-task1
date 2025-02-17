# str1 = input ("enter the string")

# res = {}
# for k in str1:
#     if k in res:
#         res[k] +=1
#     else:
#         res[k] = 1

# str2 = 
    
# print(res)

# list = ["deeksha","ammu","random"]
# final_res = []
# for names in list:
#     res = {}
#     for i in names:
#         if i in res:
#             res[i] +=1
#         else:
#             res[i] = 1

#     # print(res)
#     final_res.append({names: res})
# print(final_res)

#Second largest element
# list2 = [1,2,5,8,9,11,66,33]

# lar_ele = list2[0]
# seclar_ele = list2[0]
# for num in list2:
#     if num > lar_ele:
#         lar_ele = num
# for num in list2:
#     temp = lar_ele - num
#     if temp > seclar_ele:
      
#Disadvantage is does not work for duplicate values  and time complexity
#1st way
# list2.sort()
# print(list2)
# print(list2[-2])

#2nd way(not worked)
# lar_ele = list2[0]
# sma_ele = list2[0]

# for num in list2:
#     if num > lar_ele:
#         lar_ele = num
#     if num < sma_ele :
#           sma_ele = num


# for i in list2:
#     if i != lar_ele and i > sma_ele :

#         sec_lar_ele = i


# print(sec_lar_ele)      


# print(float(-'inf'))

list = [1,2,88,7,6,2,4,7,9,9]
unique_list = []
duplicate_list = []

for num in list:
        if num in unique_list:
           duplicate_list.append(num)
        else :
            unique_list.append(num)

print(unique_list)
print(duplicate_list)
            

        








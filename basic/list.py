list_1 = [10,21,33,40,50,50]

list_2 =["abcd","efgh"]
sum = 0

as_ci = []
for i in list_2:
    sum = 0
    for j in i:
        asci = ord(j)
        sum = sum+asci
    # sum = sum+len(i)
    as_ci.append(asci)

print(as_ci)

# for i in range(len(list_1)):
#     print(i,list_1[i])


# sum = 0

# #append - add the value into last index
# print("before append",list_1)
# list_1.append(60)
# print("after append",list_1)

# #clear = clear the all elements in a list
# # list_1.clear()

# # print("after copy",list_1)

# #copy() = copy of list to another

# list_2 = list_1.copy()
# print("after copy",list_2)

# cnt = list_1.count(50)

# count = 0
# # for i in list_1:
# #     if(i==50):
# #         count = count+1
# #     else:
# #         count = count
# # print(count)


# even_list = []
# odd_list  = []

# #team A, #team B #team C #team 
# # for i in list_1:
# #     if(i%2==0):
# #         even_list.append(i)
# #     else:
# #         odd_list.append(i)
# # print(even_list)
# # print(odd_list)

# # for i in list_1:
# #     sum = sum + i
# # print(sum)

# list_1.insert(0,100)
# print("after insert",list_1)

# #pop (), remove(),reverse(),sort, index(),extend()
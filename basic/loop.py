name = input("enter your name: ")



# print(name[0])
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    print(asc)

    # print(i) #0,1,2,3,4,5
    sum = sum + asc #115, 212, 320

print(sum)

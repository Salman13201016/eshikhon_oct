

def custom_len(x,y):
    count1 = 0
    count2 = 0
    for i in x:
        count1=count1+1
    for j in y:
        count2=count2+1
    return count1,count2

str1 = "salman"
str2 = "sultan"
a,b = custom_len(str1,str2)
print(a,b)



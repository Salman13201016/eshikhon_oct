



# print(len(list_2[1])) #[row][col]

# for i in range(5):    #i=0         i = 1         i = 2
#     for j in range(5): #j=0,1,2,3,4 ||| 0,1,2,3,4 || 0,1,2,3,4.....
#         print(i,j)


list_2 = [[1,2,3],[4,5],[7,8,9],[10,11,12]]
num_of_rows = len(list_2) #4

# for row in range(num_of_rows): #row = 0;1;
#     col_size = len(list_2[row])  #col_size = 3,2
#     for col in range(col_size):
#         print(list_2[row][col]) #0,0 #0,1 #0,2; #0,0 #0,1

for row in list_2: #row = 0;1;
    print(row)
    for col in row:
        print(col) #0,0 #0,1 #0,2; #0,0 #0,1




#===========================Without list comprehension====================================================
listijk = [] #an empty list to be filled as following
x = 2
y = 1
z = 1
for i in range(x + 1): #it will output 0, and will only output 1 after the next conditions ('for j' and 'for k') are met.
    for j in range (y + 1): #it will output 0, and will only output 1 after the next condition ('for k') is met.
        for k in range (z + 1): #it will output 0 and then 1.
            #if i+j+k!=3:
            listijk.append([i, j, k])  # it will add i, j and k values to the list
print(listijk) #print the list properly filled
print([[i,j,k] for i,j,k in listijk if i+j+k!=3])



#==========================Using list comprehension===========================================================
x,y,z,n = int(input()),int(input()),int(input()),int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
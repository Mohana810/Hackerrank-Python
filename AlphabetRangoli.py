
# string = 'abcdefgh'
# print(string[-2:])


#[-1:] -> only the last letter, [-2:] -> only the last two letters and so on
#[:-1] -> everything except the last letter
#[::-1] -> reverses the entire string


#================================================solution==============================================

def print_rangoli(n): #n=5
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]  #list of the first n alphabets = [a,b,c,d,e]
    items = list(range(n))  # list of first n integers (for indices) = [0,1,2,3,4]
    items = items[:-1]+items[::-1] # adding two lists where the first list has all the elements except the last
                                   # and the second list has the reversed elements order = [0,1,2,3|4,3,2,1,0]
    for i in items:
        temp = data[-(i+1):] # temp = [e]; temp = [d,e]
        row = temp[::-1]+temp[1:] # row = [e]; row = [e,d]+[e]=[e,d,e]
        print("-".join(row).center(n*4-3, "-")) #join the elements of row with '-', brin it to the centre and
                                                # then add 4*n-3 '-'

n = int(input())
print_rangoli(n)
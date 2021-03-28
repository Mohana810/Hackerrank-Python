n, m = map(int, input().split())
c = '.|.'

for i in range(1,n,2):
    print((i * c).center(m, "-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,-1,-2):
    print((i *c).center(m, "-"))

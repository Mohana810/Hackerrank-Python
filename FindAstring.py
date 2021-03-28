s = input()
sub = input()
cnt = 0
while sub in s:
    cnt += 1
    s = s[s.find(sub)+1:]
    #print(s)
print(cnt)

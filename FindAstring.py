# #from collections import Counter
#
# string = 'mohanasrana'#input().strip()
# substring = 'aan' #input().strip()
#
# while substring in string:
#     print(substring)
#     string = string[string.find(substring)+1:]
#
# # string = string[string.find('ana')+1:]
# # print(string)
s = input()
sub = input()
cnt = 0
while sub in s:
    cnt += 1
    s = s[s.find(sub)+1:]
    #print(s)
print(cnt)
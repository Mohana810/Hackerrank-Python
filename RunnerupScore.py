score = list()
n = int(input())
for _ in range(n):
    sc = int(input())
    score.append(sc)
score = sorted(score,reverse=True)
m = max(score)
for i in range(n):
    if score[i]!=m:
        print(score[i])
        break

#===========================When the input of numbers is given in single line===================================
n = int(input())
arr = map(int, input().split())
arr = sorted(arr,reverse=True)
m = max(arr)
for i in range(n):
    if arr[i]!=m:
        print(arr[i])
        break

record = list()
names = list()
scores = set() # set does not use duplicate values

N = int(input())
for _ in range(N):
    name = input()
    grade = float(input())
    record.append([name, grade])
    scores.add(grade)

second_lowest = sorted(scores)[1]

for n, g in record:
    if g == second_lowest:
        names.append(n)

for n in sorted(names):
    print(n)


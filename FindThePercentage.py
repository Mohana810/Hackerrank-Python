n = int(input())
student_marks = dict()
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# a,b,c = student_marks[query_name]
print('%.2f' % (sum(student_marks[query_name]) / 3))
# print(float(sum(student_marks[query_name])/3))  This line will give only one digit                                                       after decimal

student_list = []
for _ in range(28):
    student_number = int(input())
    student_list.append(student_number)
student_list.sort()

for i in range(1, 31):
    if i not in student_list:
        print(i)

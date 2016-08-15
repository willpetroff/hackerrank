"""
Given a list of students and grades, return the name(s) of the student(s) with the second lowest grade.
"""

student_list = []
student_num = int(input())
for _ in range(student_num):
    student_name = input()
    student_grade = float(input())
    student_list.append([student_name, student_grade])
student_list.sort(key=lambda student: student[1])
smallest = student_list[0][1]
index_value = 1
while student_list[index_value][1] == smallest:
    index_value += 1
ret_list = [student_list[index_value][0]]
for index in range(index_value+1, student_num):
    if student_list[index_value][1] == student_list[index][1]:
        ret_list.append((student_list[index][0]))
ret_list.sort()
for item in ret_list:
    print(item)

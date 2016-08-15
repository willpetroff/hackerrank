"""
Output the average of an asked-for student to two decimal places.
"""

student_num = int(input())
grade_dict = {}
for i in range(student_num):
    student_line = input()
    grade_dict[student_line.split()[0]] = student_line.split()[1:]
requested_student = input()
if requested_student in grade_dict:
    print('{0:.2f}'.format(sum([float(i) for i in grade_dict[requested_student]])/len(grade_dict[requested_student])))
else:
    print('{0:.2f}'.format(0))

marks = [85, 92, 78, 96, 45, 67, 88, 54, 72, 90]
print('Student Marks:' , marks)
count=0
avearge_marks=sum(marks)/len(marks)
height_marks=max(marks)
lowest_marks=min(marks)

for i in marks:
    if i >40:
        count=count+1
        

print('Average Marks: ',avearge_marks)
print('Highest Marks: ',height_marks)
print('Lowest Marks: ',lowest_marks)
print('Passed Students: ',count)
print('Grades:')

for mark in marks: 
    if mark >= 90:
        Grade ='A'
    elif mark >= 75 and mark < 90:
        Grade='B'
    elif mark >= 50 and mark < 75:
        Grade='C'
    else:
        Grade='Fail'

    print(f'{mark} : {Grade}')


   

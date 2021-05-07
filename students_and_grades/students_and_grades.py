numberOfStudents = input('How many students do you have?')

studentName = input('Student name:')

studentGrade = input('Student grade:')

# try: studentGrade = int
# except ValueError:
#     print("Must be a number.")

selectACourse = input('Select a course: 1 - Math, 2 - Science, 3 - History:')


# for i in selectACourse:
#     print(i)

print('Name: ', studentName, 'Grade: ', studentGrade, 'Course: ', selectACourse)
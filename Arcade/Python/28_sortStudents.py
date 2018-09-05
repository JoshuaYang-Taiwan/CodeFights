def sortStudents(students):
    students.sort(key=lambda x : x.split(' ')[-1])
    return students

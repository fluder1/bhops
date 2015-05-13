import json

class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        if (grade.lower() == "senior"):
            self.grade_rank = 4
        elif (grade.lower() == "junior"):
            self.grade_rank = 3
        elif (grade.lower() == "sophomore"):
            self.grade_rank = 2
        else:
            self.grade_rank = 1
    def __repr__(self):
        return repr((self.first_name, self.last_name, self.grade))    

with open ("students.json", "r") as jsonFile:
    rawStudentData = jsonFile.read()
        
studentList = []
rawStudentData = rawStudentData.split("}")

for line in rawStudentData:
    entryByLine = line.split()
    try: 
        grade = entryByLine[2].strip('\",')
        first_name = entryByLine[4].strip('\",')
        last_name = entryByLine[6].strip('\"')
        studentList.append(Student(first_name, last_name, grade))
    except IndexError:
        continue

studentList = sorted(studentList, key=lambda student: student.grade_rank)
sortedDataFile = open('sortedData', 'w')
for i in range(len(studentList)):
    sortedDataFile.write(str(studentList[i]))
sortedDataFile.close()

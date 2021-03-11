students = []
def readmodules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["Modules"]= readmodules()
    students.append(currentStudent)

doAdd(students)
doAdd(students)

print(students)
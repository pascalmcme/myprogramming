student = {"Name":"Mary Byrne",

"modules":[

{"courseName":"Programming", "Grade":71 },
{"courseName":"Science", "Grade":72 }

]   #modules are changeable list of dict items



}


print('Student: {}' .format(student["Name"])) # use square brackets to call and element from dict
for module in student["modules"]:
    print('Course Name: {} \nGrade: {}' .format(module["courseName"],module["Grade"]))

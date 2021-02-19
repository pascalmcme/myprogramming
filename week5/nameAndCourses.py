student = {"Name":"Mary Byrne",

"modules":[

{"courseName":"Programming", "Grade":71 },
{"courseName":"Science", "Grade":72 }

]   #modules are changeable list



}


print('Student: {}' .format(student["Name"])) # use square brackets to call and element from dict
for module in student["modules"]:
    print('Grade: {}' .format(module["Grade"]))

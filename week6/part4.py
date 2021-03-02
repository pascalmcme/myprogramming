


def readModules():
 modules = []
 moduleName = input('enter module name: ')
 while moduleName != "":
     module = {}   
     module ["Name"] = moduleName 
     module ["Grade"] = int(input('enter grade:'))
     modules.append(module)
     moduleName = input('enter module name (blank to quit): ')
 #print(modules)
 return modules
 

readModules()





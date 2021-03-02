


def displayMenu():
 print('What would you like to do? \n (a) Add new student \n (v) View students \n (q)Quit')
 choice = input(('Type one letter (a/v/q):')).strip()
 
 return choice 
 

def doAdd():
    print('In adding')

def doView():
    print('In view')

#Main Part
choice = displayMenu()
while (choice != 'q'):

 if choice == 'a':
    doAdd()
 elif choice == 'v':
    doView()
 else:
     print("\n please selevt either a, v or q")
 choice = displayMenu()

 


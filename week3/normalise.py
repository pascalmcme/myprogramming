# Please enter a string: Some StRiNg
#That String normalised is :some string
#we reduced the input string from 57 to 11 characters

#lower () - write in lower case

string = input('please enter a string:')
stringlowercase = string.lower()
stringnoleading =stringlowercase.strip()
# stingnormalised = string.lower() .strip()
lenghtstring =len(string)
lenghtstringnoleading=len(stringnoleading)


print('The string normalised is {}' . format(stringnoleading))
print('We reduced the input string from {} to {} characeters'. format(lenghtstring,lenghtstringnoleading))
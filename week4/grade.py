percentage = int(input('Enter a percentage:'))


if  percentage <0 or percentage >100:
 print('please enter a number between 0 and 100')


elif percentage <= 40:
 print('Fail')

elif percentage >= 40 and percentage <= 49:
 print('Pass')


elif percentage >= 50 and  percentage <=59:
 print('Merit 2')

 
elif percentage >= 60 and percentage <=69:
 print('Merit 1')

 
elif percentage >=70:
 print('Distinction')

#Bonus 1.
# rawpercentage = int(input('Enter a percentage:'))
# percewntage = int(round(rawpercentage))
# https://stackoverflow.com/questions/31818050/round-number-to-nearest-integer
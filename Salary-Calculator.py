sal = int(input('Enter your salary: '))

x = [''] * int(input('\nhow much expenses do you have? '))
for i in x:
	i = int(input('Enter price: '))
	sal = sal - i 
print('\nChange left: ', sal)

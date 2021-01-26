sal = int(input('Enter your salary: '))
sal1 = sal
Dollar = sal // 3.75
expenses = {}
for l in range(1, int(input('\nhow much expenses do you have? '))+1):
	l = input('what is your expenses: ')
	expenses[l] = 'hi'
print('\n')	
total_expenses = 0
for i in expenses:
	i = int(input('How much '+str(i)+' price? '))
	total_expenses = total_expenses + i
	sal = sal - i
Dollar1 = sal // 3.75
total_expenses1 = total_expenses // 3.75
print('\nyour salary: '+str(sal1)+'SAR')
print('your expenses: '+str(total_expenses)+'SAR')
print('Salary left: '+str(sal)+'SAR')
print('\nyour salary with Dollar: '+str(Dollar)+'$')
print('your expenses: '+str(total_expenses1)+'$')
print('Salary left: '+str(Dollar1)+'$')

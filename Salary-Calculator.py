sal = int(input('Enter your salary: '))

expenses = {}

for l in range(1, int(input('\nhow much expenses do you have? '))+1):
	l = input('what is your expenses: ')
	expenses[l] = 'hi'
print('\n')	
for i in expenses:
	i = int(input('How much '+str(i)+' price? '))
	sal = sal - i

print('\nSalary left: '+str(sal)+'SAR')

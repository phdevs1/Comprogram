i = 0
while True:
	letter = input()
	i = i + 1
	if letter == '*':
		break;
	elif letter == 'Hajj':
		print ( 'Case ' + str(i)+ ': ' + 'Hajj-e-Akbar')
	elif letter == 'Umrah':
		print ('Case ' + str(i)+ ': ' +'Hajj-e-Asghar')

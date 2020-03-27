repeat = int(input())

for _ in range(repeat):
	s = input()
	if s == '1' or s == '4' or s == '78':
		print ('+')
	elif s[-2:] == '35':
		print ('-')
	elif s[0] + s[-1] == '94' :
		print ('*')
	elif s[0:3] == '190':
		print ('?')

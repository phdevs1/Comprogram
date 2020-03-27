k = int(input());
while k != 0:
	n,m = map(int,input().split());
	for i in range(k):
		x,y = map(int,input().split());
		if x-n == 0 or y-m == 0:
			print("divisa");
		elif x-n > 0:
			if y-m > 0:
				print("NE");
			else:
				print("SE");
		elif x-n < 0:
			if y-m > 0:
				print("NO");
			else:
				print("SO");
	k = int(input());




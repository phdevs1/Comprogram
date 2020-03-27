n = int(input())
if n<=10:
	for _ in range(n):
		c = 0;
		w = input();
		if len(w) == 5:
			print(3)
		else:
			if w[0] == 'o':
				c+=1;
			if w[1] == 'n':
				c+=1;
			if w[2] == 'e':
				c+=1;
			if c>=2:
				print(1);
			else:
				print(2);

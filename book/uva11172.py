t = int(input());
while t>0 and t<15:
	a,b = map(int,input().split())
	if a > b:
		print(">");
	elif a < b:
		print("<");
	else:
		print("=");
	t=t-1;

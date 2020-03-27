c = int(input());

while c>0:
	v1,v2 = input().split();
	v1 = int(int(v1)/3);
	v2 = int(int(v2)/3);
	print(v1*v2);
	c=c-1;
	
t = int(input());

for i in range(t):
	l,w,h = list(map(int,input().split()));
	if l<=20 and w<=20 and h<=20:
		print("Case %d: good" % (i+1));
	else:
		print("Case %d: bad" % (i+1));

t = int(input());
for i in range(t):
	salary = list(map(int,input().split()));
	salary.sort();
	print("Case %i: %i" % (i+1,salary[1]));

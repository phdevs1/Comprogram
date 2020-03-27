n = int(input());
count = 1;
while n!=0:
	supd = 0;
	give = 0;
	ev = input().split();
	ev = list(map(int,ev));
	for ele in ev:
		if ele==0:
			give+=1;
		else:
			supd+=1;
	print("Case %d: %d" % (count,supd-give));
	n = int(input());
	count+=1;
t = int(input());
if t>0 and t<=100:
	for i in range(t):
		n = int(input());
		r = abs((((((n*567)/9)+7492)*235)/47)-498)
		m = (int(r%100))//10
		print(m);


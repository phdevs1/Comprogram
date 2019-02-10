val = int(input());
bill = [100,50,20,10,5,2,1]

i=0;
print(val);
while len(bill)>i:
	c=0;
	while val>=bill[i]:
		val = val - bill[i];
		c+=1;
	print("%i nota(s) de R$ %i,00" % (c,bill[i]));
	i+=1;


a = float(input());


bills = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01];


i=0;
print("NOTAS:")
while i<=len(bills)-1:
	c=0;
	
	while a >= bills[i]:
		a=a-bills[i];
		c+=1;
		a=round(a,2);
		

	if bills[i]==1:
		print("MOEDAS:")
	if bills[i]>1:
		print("%i nota(s) de R$ %.2f" % (c,bills[i]));
	else:
		print("%i moeda(s) de R$ %.2f" % (c,bills[i]));
	i+=1;
	a=round(a,2);
	
	
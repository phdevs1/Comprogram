a = float(input());
#new_value = "{:.2f}".format(value)

mount = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01];



def quantity_list(val,pos):
	div = val/mount[pos];
	mod = val%mount[pos];
	mod = round(mod,2);
	if pos==6:
		print("MOEDAS:")
	if pos< 6:
		print("%i nota(s) de R$ %0.2f" % (int(div),mount[pos]))
	else:
		print("%i moeda(s) de R$ %0.2f" % (int(div),mount[pos]))
	new_mod = int(mod);
	if mount[pos] ==0.01:
		return 0;
	if mod > mount[pos+1]:
		return quantity_list(mod,pos+1);
	else:
		if pos+1==6:
			print("MOEDAS:")
		if pos+1<= 6:
			print("%i nota(s) de R$ %0.2f" % (0,mount[pos+1]))
		else:
			print("%i moeda(s) de R$ %0.2f" % (0,mount[pos+1]))
		return quantity_list(mod,pos+2);


print("NOTAS:")
a = round(a,2);
quantity_list(a,0);

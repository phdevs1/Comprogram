val = int(input());

if val>3600:
	h = val/3600;
	hm = val%3600;
	val = hm;
else:
	h = 0;
if val>60:
	m = val/60;
	mm = val%60;
	s=mm;
else:
	m=0;
	s=val;

print("%i:%i:%i" % (h,m,s));
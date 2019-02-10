import math as m
a,b,c = input().split();
a,b,c = [float(x) for x in [a,b,c]];

d = pow(b,2)-4*a*c;

if d<0 or a==0.0:
	print("Impossivel calcular");
else:
	r1 = (-b+m.sqrt(d))/(2*a);
	r2 = (-b-m.sqrt(d))/(2*a);
	print("R1 = %.5f" % r1);
	print("R2 = %.5f" % r2);
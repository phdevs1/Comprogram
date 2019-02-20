h,m = input().split(':')

h = int(h);
m = int(m);
while(h!=0 or m!=00):
	h_ang = 30*(h+m/60);
	m_ang = m*6;
	
	dif_ang = abs(m_ang - h_ang);
	if dif_ang>180:
		dif_ang = 360 - dif_ang;
	print("%.3f" % dif_ang);
	h,m = input().split(':')
	h = int(h);
	m = int(m);

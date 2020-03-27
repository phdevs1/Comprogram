i,a,b,c = input().split();
i,a,b,c = [int(x) for x in [i,a,b,c]];

while i!=0 or a!=0 or b!=0 or c!=0:
	su = 1080+ ((i-a+40)%40+(b-a+40)%40+(b-c+40)%40)*9
	print(su);
	i,a,b,c = input().split();
	i,a,b,c = [int(x) for x in [i,a,b,c]];



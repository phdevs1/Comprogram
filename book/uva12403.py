t = int(input());
c = 0;
for _ in range(t):
	m = list(input().split());
	if m[0] == "donate":
		k = int(m[1])
		c = c + k;
	if m[0] == "report":
		print(c);
		
months,downpay,loan,n_dep = map(float,input().split())
list_dps = []
Car_0 = loan + downpay


for _ in range(int(n_dep)):
	mth,dpre = map(float,input().split())
	list_dps.append((int(mth),dpre))

c_month = 0
pos = 0
while 1:
	if c_month == list_dps[pos][0]:
		Car_0 = Car_0 * (1 - list_dps[pos][1])
		c_month += 1
		pos += 1
	else:
		Car_0 = Car_0 * (1 - list_dps[pos - 1][1])
		c_month += 1

	loan = loan - loan/months
	
	print (Car_0)
	print (pos)
	if len(list_dps) - 1 < pos :
		break
	if Car_0 > loan:
		break



print (c_month )

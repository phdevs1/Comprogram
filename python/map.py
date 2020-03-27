def es_par(n):
	return (n%2.0==0)

l=[1,2,3,4]

l2 = filter(es_par,l)

print(list(l2))
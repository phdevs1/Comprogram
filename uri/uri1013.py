a,b,c = input().split();
a,b,c = [int(x) for x in [a,b,c]];

m1 = (a+b+abs(a-b))/2

m2 = (m1+c+abs(m1-c))/2

print("%i eh o maior" % m2);
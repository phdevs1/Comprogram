n1,n2,n3,n4 = input().split();
n1,n2,n3,n4 = [float(x) for x in [n1,n2,n3,n4]];


media = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1);
print("Media: %.1f" % media);


if media>=7.0:
	print("Aluno aprovado.");
elif media<5.0:
	print("Aluno reprovado.");
elif media>=5.0 and media<=6.9:
	print("Aluno em exame.");
	n5 = input();
	n5 = float(n5);
	print("Nota do exame: %.1f" % n5);
	media2 = (media+n5)/2;
	if media2>=5.0:
		print("Aluno aprovado.")
	elif media2<=4.9:
		print("Aluno reprovado")
	print("Media final: %.1f" % media2);







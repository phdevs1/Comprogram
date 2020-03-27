c = 0;
while True:
	try :
		text = input()
	except EOFError:
		break
	new_txt = [];
	for i in text:
		if i == "\"":
			if c==0:
				new_txt.append("``");
				c=1;
			else:
				new_txt.append("''");
				c=0;
		else:
			new_txt.append(i);
	print("".join(new_txt));
			
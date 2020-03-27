count = 1;
while 1:
	wd = input();
	if wd == '#':
		break;
	if wd == 'HELLO':
		print("Case %d: ENGLISH" % count);
		count=count+1;
	elif wd == 'HOLA':
		print("Case %d: SPANISH" % count);
		count=count+1;
	elif wd == 'HALLO':
		print("Case %d: GERMAN" % count);
		count=count+1;
	elif wd == 'BONJOUR':
		print("Case %d: FRENCH" % count);
		count=count+1;
	elif wd == 'CIAO':
		print("Case %d: ITALIAN" % count);
		count=count+1;
	elif wd == 'ZDRAVSTVUJTE':
		print("Case %d: RUSSIAN" % count);
		count=count+1;
	else:
		print("Case %d: UNKNOWN" % count);
		count=count+1;


def greet(lang):
	def g_spa():
		print("holas")
	def g_eng():
		print("hi")
	def g_bra():
		print("garoto")
	def no():
		print("no existe")
	lang_select = {
				"es":g_spa,
				"en":g_eng,
				"po":g_bra
				}
	return lang_select.get(lang,no)



la = input("ingresa el idioma: ")

greet(la)()



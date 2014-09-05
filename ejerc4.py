def ValorCadena(x,y):
	if len(x)==len(y):
		print x+y
	else:
		if len(x)>len(y):
			print x
		else:
			print y


cad1=raw_input("Ingrese palabra1: ")
cad2=raw_input("Ingrese palabra2: ")
ValorCadena(cad1,cad2)

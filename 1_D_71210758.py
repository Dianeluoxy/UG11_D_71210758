string = input("Masukkan string : ")

def cekString(string):
	if string.replace(".","").isnumeric() == True:
		if float(string)%2 == 0:
			print(format(float(string)/2, ".0f"))
		else :
			print(format((round(float(string))+5)/2, ".0f"))
	else:
		print(string[::-1])

cekString(string)
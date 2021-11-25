string = input("Masukkan sebuah kata/kalimat : ")
karakter = input("Masukkan karakter yang ingin disisipkan : ")

def sisipHuruf(karakter, string):
	print(string.upper().replace('',(" %s " %karakter)).rstrip((" %s ") %karakter).lstrip((" %s ") %karakter))

def sisipKata(karakter, string):
	print(string.title().replace(" ",(" %s " %karakter)))

sisipHuruf(karakter, string)
sisipKata(karakter, string)
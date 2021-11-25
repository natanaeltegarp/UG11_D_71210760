str=input("Masukkan string: ")

def cekString(str):
    if str.isdigit():
        angka=int(str)
        if angka%2==0:
            angka=int(angka/2)
            print(angka)
        else:
            angka=int((angka+5)/2)
            print(angka)
    else:
       str=str[::-1]
       print(str)
cekString(str)
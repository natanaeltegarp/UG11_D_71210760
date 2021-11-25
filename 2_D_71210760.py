str=input("Masukkan sebuah kata/kalimat: ")
sisip=input("Masukkan karakter yang ingin disisipkan: ")

def sisipHuruf(str,sisip):
    cap=str.upper()
    print(sisip.join(list(cap)))
def sisipKata(str,sisip):
    cap=str.title()
    print(sisip.join(cap.split()))

sisipHuruf(str,sisip)
sisipKata(str,sisip)
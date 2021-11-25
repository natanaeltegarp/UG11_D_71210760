import random


def generatesoal(tipe,soal):
    bil1=random.randint(1,20)
    bil2=random.randint(1,20)
    bil3=random.randint(1,20)
    bil4=random.randint(1,20)
    perbandingan = ['<','>','==']
    random_perbandingan=random.choice(perbandingan)
    if tipe=="penjumlahan":
        soal=bil1 + bil2, random_perbandingan, bil3 + bil4
        print('(benar/salah) jika ', bil1, '+', bil2, random_perbandingan, bil3, '+', bil4)
    elif tipe=="pengurangan":
        soal=bil1 + bil2, random_perbandingan, bil3 + bil4
        print('(benar/salah) jika ', bil1, '-', bil2, random_perbandingan, bil3, '-', bil4)
def cekHasil(soal,jawaban):
    if jawaban =="benar":
        if soal == True:
            print("Jawaban Anda Benar !")
        else:
            print("Jawaban Anda Masih Salah !")
    if jawaban =="salah":
        if soal == False:
            print("Jawaban Anda Benar !")
        else:
            print("Jawaban Anda Masih Salah !")

tipe=input("Masukkan tipe yang ingin anda coba: ")
tipe=tipe.lower()
soal=0
generatesoal(tipe,soal)
jawaban=input("Masukkan jawaban anda: ")
jawaban=jawaban.lower()
print(soal)
cekHasil(soal,jawaban)
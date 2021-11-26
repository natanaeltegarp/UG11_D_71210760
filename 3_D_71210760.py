import random


def generatesoal(tipe):
    bil1=random.randint(1,20)
    bil2=random.randint(1,20)
    bil3=random.randint(1,20)
    bil4=random.randint(1,20)
    perbandingan = ['<','>','==']
    random_perbandingan=random.choice(perbandingan)
    global soal
    soal=True
    if tipe=="penjumlahan":
        if random_perbandingan=='<':
            soal=bil1 + bil2 < bil3 + bil4
        elif random_perbandingan=='>':
            soal=bil1 + bil2 > bil3 + bil4
        else:
            soal=bil1 + bil2 == bil3 + bil4
        print('(benar/salah) jika ', bil1, '+', bil2, random_perbandingan, bil3, '+', bil4)
    elif tipe=="pengurangan":
        if random_perbandingan=='<':
            soal=bil1 - bil2 < bil3 - bil4
        elif random_perbandingan=='>':
            soal=bil1 - bil2 > bil3 - bil4
        else:
            soal=bil1 - bil2 == bil3 - bil4
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
generatesoal(tipe)
jawaban=input("Masukkan jawaban anda: ")
jawaban=jawaban.lower()
cekHasil(soal,jawaban)
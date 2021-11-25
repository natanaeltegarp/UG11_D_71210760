import random

def tabakangka(a,b):
    acak=random.randint(a,b)
    global angka
    angka=acak
    print("Apakah ", angka, "?")

mini=1
maks=7
mulai=input("Untuk memulai program masukkan (-1) untuk memulai: ")
if mulai == "-1":
    tabakangka(mini,maks)
    jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
    if jawaban == "0":
        tabakangka(mini,angka-1)
        print("Jumlah tebakan : 2")
        jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
        if jawaban == "0":
            tabakangka(mini,angka-1)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "1":
            tabakangka(angka+1,maks)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "2":
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 2 \nProgram selesai")
    elif jawaban == "1":
        tabakangka(angka+1,maks)
        print("Jumlah tebakan : 2")
        jawaban=input("Apakah sudah benar? \nLebih kecil (0) \nLebih besar (1) \nbenar (2) \n:")
        if jawaban == "0":
            tabakangka(mini,angka-1)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "1":
            tabakangka(angka+1,maks)
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 3 \nProgram selesai")
        elif jawaban == "2":
            print("hasil penjumlahannya pasti ", angka)
            print("Jumlah tebakan : 2 \nProgram selesai")
    elif jawaban == "2":
        print("hasil penjumlahannya pasti ", angka)
        print("Jumlah tebakan : 1 \nProgram selesai")
else:
    print("program tidak berhasil dijalankan")
#Tanpa Parameter
# def menu():
#     print("Menu Pilihan")
#     print("1. Tambah")
#     print("2. Kurang")
#     print("3. Kali")
#     print("4. Bagi")  
# menu()

# def salam():
#     print ("Selamat Pagi, FT Muda")
# def kali():
#     x = 6*4
#     print(x)
# salam()
# kali()

#Dengan Parameter
# def salam(nama):
#     print("Selamat Pagi", nama)
# salam("Ridho")

# def tambah(a,b):
#     hasil = a + b
#     print(hasil)
# tambah(6,4)

#Jika Memakai Input Dengan Parameter
# a = int(input("Masukkan Angka Pertama : "))
# b = int(input("Masukkan Angka Kedua : "))
# def tambah(a,b):
#     hasil = a + b
#     print(hasil)
# tambah(a,b)

#Jika Memakai Input Tanpa Parameter
# def penjumlahan():
#     a = int(input("Masukkan Angka Pertama : "))
#     b = int(input("Masukkan Angka Kedua : "))
#     hasil = a + b
#     print(hasil)
# penjumlahan()

#Fungsi
# a = int(input("Masukkan Angka Pertama : "))
# b = int(input("Masukkan Angka Kedua : "))
# def tambah(a,b):
#     hasil = a + b
#     return hasil
# print(tambah(a,b))

#Variabel Lokal & Global
#Global
# nama = "Shandy"
#Lokal
# def salam():
#     nama = "Ibnu"
#     print(nama)
#Memanggil Variabel
# print(nama)
# salam()

#Rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
#Rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
#Pemanggilan Fungsi
# volume_persegi(6)

#Contoh CRUD
# buku = []
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
            
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)
    
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru
        
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])
        
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")
# while(True):
#     show_menu()
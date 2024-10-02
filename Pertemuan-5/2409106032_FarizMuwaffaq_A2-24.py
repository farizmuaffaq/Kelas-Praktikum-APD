# LIST
# nama = ["Celio","Afrizal","Farrel","Ghazali","Vito"]
# print("sebelum")
# print(nama)
# print("")
# nama.append("Afrizal")
# print("sesudah")
# print(nama)

# nama = ["Celio","Afrizal","Farrel","Ghazali","Vito"]
# print("sebelum")
# print(nama)
# print("")
# # nama.insert("2,Afrizal")
# print("sesudah")
# # print(nama)
# nama[4]= "fufufafa"
# print(nama)

# nama = ["Celio","Afrizal","Farrel","Ghazali","Vito"]
# print("sebelum")
# print(nama)
# print("")
# print("sesudah")
# hapus = nama.pop(2)
# print(nama)
# print(hapus)

# nama = ["Celio","Afrizal","Farrel","Ghazali","Vito"]
# print(nama[0:2])

# nama = ["Celio","Shandy","Farrel","Ghazali","Vito","Yuyun","Adri","Rizal","Adi","Ifnu"]
# print("sebelum")
# print(nama)
# print("")
# print("sesudah")
# print(nama[1:8:2])

# nama = ["Celio","Shandy","Farrel","Ghazali","Vito","Yuyun","Adri","Rizal","Adi","Ifnu"]
# matkul = ["APD","APL","JARKOM","STRUKDAT","WEB"]
# data = nama+matkul
# print("sebelum")
# print(nama)
# print("")
# print("sesudah")
# print(data)

# data = ["farel","celio",[1,2,["halo",23,2.3,True]]]
# # print(data[2][2][3:])
# print(data[::-1])

# angka = [1,2,3,4,[5,6,7,[8,9,0]]]
# print(angka[4][3][2:])

# matkul = [(1,2,3),(4,5,6),(7,8,9)]
# for i in matkul:
#     for j in i:
#         print(j)


# TUPLE

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print(absen)
# print(prodi)
# print(nim)
# print(nama)

print(
"""
==========================
|   DATA MAHASISWA A24   |
==========================
|    1. TAMBAH DATA      |
|    2. TAMPILKAN DATA   |
|    3. UBAH DATA        |
|    4. HAPUS DATA       |
|    5. KELUAR           |
==========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")
#Kalkulator Sederhana
print("""
      ====================
      1. +
      2. -
      3. *
      4. /
      ====================
      """)
fitur = int(input("Pilih Fitur : "))
match fitur:
    case 1:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a + b
        print(f"Hasil penjumlahan angka 1 dan angka 2 adalah {c}")
    case 2:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a - b
        print(f"Hasil pengurangan angka 1 dan angka 2 adalah {c}")
    case 3:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a * b
        print(f"Hasil perkalian angka 1 dan angka 2 adalah {c}")
    case 4:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a / b
        print(f"Hasil pembagian angka 1 dan angka 2 adalah {c}")
    case _:
        print("Salah input bang")

#Menentukan Ganjil Genap
 angka = int(input("Masukkan angka: "))
 result = "Genap" if angka % 2 == 0 else "Ganjil"
 print(angka, "adalah angka",result)

#Menentukan Jenis Kelamin Dengan Ternary Operator
jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :")
hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"
print(hasil)
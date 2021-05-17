def tambah(peserta, nama):
    if nama in peserta:
        peserta[nama] += 1
    else:
        peserta[nama] = 1

# inisiasi dictionary nama peserta webinar
peserta = dict()
# inisiasi jumlah peserta webinar
for i in range(3):
    jumlah = int(input(f"Jumlah nama yang akan dicatat untuk Webinar {i+1}: "))
    for j in range(jumlah):
        nama = input(f"Masukkan nama {j+1}: ")
        tambah(peserta, nama)
    print()
# cetak daftar hadir
print("Peserta yang datang ke Webinar Donat DUAARRR!!!:")
# gabungkan dict menjadi string
peserta_string = ', '.join(f'{key}({val})' for key,val in peserta.items() if key)
print(peserta_string) if (peserta_string) else print("Tidak Ada")
print()
# cetak yang hadir di seluruh webinar
print("Peserta yang datang ke seluruh Webinar Donat DUAARRR!!!:")
peserta_komplit_string = ', '.join(key for key,val in peserta.items() if key and val == 3)
print(peserta_komplit_string) if (peserta_komplit_string) else print("Tidak Ada")
# Program: The Eligma Code (Challenge)
# Informasi: decimal value A-Z adalah 65-90,
#            decimal value a-z adalah 97-122,
#            decimal value 0-9 adalah 48-57
# Program ini dibuat oleh Muhammad Athallah (2020)

# Bagian input
kalimat_masukan = input("Masukkan string: ")

# Bagian Pemisah
kalimat_bersih = ""  # Inisiasi wadah untuk kalimat tanpa angka
angka_dekripsi = 0  # Inisiasi wadah untuk angka dekripsi
for char in kalimat_masukan:
    if 64 < ord(char) < 91 or 96 < ord(char) < 123:  # Mengecek apakah karakter merupakan alfabet
        kalimat_bersih += char  # Tambahkan ke kalimat
    else:  # Karena dijamin tidak ada karakter selain A-Z, a-z dan 0-9
        angka_dekripsi += ord(char) - 48  # Berdasarkan informasi nilai angka

# Bagian Dekripsi
kalimat_keluaran = ""  # Inisiasi wadah untuk kalimat yang terdekripsi
for char in kalimat_bersih:
    char_awal = ord(char)
    char_temp = ord(char) + angka_dekripsi  # Geser nilai karakter
    # Mekanisme geser z ke A
    if char_temp > 122:  # Apabila di luar range a-z
        char_temp -= 58  # "Lempar" ke A-Z
    elif char_temp > 90 and char_awal < 97:  # Apabila di luar range A-Z
        char_temp += 6  # "Lempar" ke a-z
    kalimat_keluaran += chr(char_temp)  # Tampung ke kalimat_keluaran

# Bagian Output
print(kalimat_keluaran)
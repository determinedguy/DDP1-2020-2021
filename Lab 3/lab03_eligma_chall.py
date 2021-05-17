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
    char_temp = ord(char) + angka_dekripsi  # Geser nilai karakter
    # Mekanisme geser z ke A
    if char_temp > 122 and 96 < ord(char) < 123:  # Apabila di luar range a-z
        if (angka_dekripsi / 26) % 2 != 0:
            while char_temp > 90:
                char_temp -= 58  # "Lempar" ke A-Z
        else:
            while char_temp > 122:
                char_temp -= 26  # Balikkan ke a-z
    elif char_temp > 90 and 64 < ord(char) < 91:  # Apabila di luar range A-Z
        if (angka_dekripsi / 26) % 2 != 0:
            char_temp += 6  # "Lempar" ke a-z
            while char_temp > 122:  # Kalau terlalu gede, thanks to Nito dan Faishol
                char_temp -= 26
        else:
            while char_temp > 90:
                char_temp -= 26  # Balikkan ke A-Z
    '''
    Kalau angka_dekripsi dibagi 26 dan hasil_bagi ganjil,
    maka emang naik tingkat. (AZ ke az, vice versa).
    Kalau angka_dekripsi dibagi 26 dan hasil_bagi genap,
    maka tingkatnya tetap. (AZ ya AZ, az ya az).

    AYAAA FAISHOL AYA-AYA WAEE :((
    Makasih lho overthinkingnya /hiks/
    '''
    kalimat_keluaran += chr(char_temp)  # Tampung ke kalimat_keluaran

# Bagian Output
print(kalimat_keluaran)
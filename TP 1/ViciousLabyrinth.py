# Nama Program: Vicious Labyrinth
# Info: ​Ternary​ merupakan basis 3, sedangkan ​septenary​ merupakan basis 7
# Program ini dibuat oleh Muhammad Athallah (2020)
# Program ini diselesaikan pada 3 Oktober 2020, pukul 18:47 WIB

# Bagian Fungsi


def operasi_decimal(angka):
    string_keluaran = ""  # Untuk menampung hasil konversi
    # Handling Angka 0
    if angka == 0:
        string_keluaran += str(angka)
    # Operasi Pembagian
    # Sumber mekanisme: https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
    while angka:
        angka, hasil_bagi = divmod(angka, basis_tujuan)  # Bagi dan cari modulo dari angka
        string_keluaran += str(hasil_bagi)  # Kumpulkan sisa bagi
    string_keluaran = string_keluaran[::-1]  # Balik keluaran (karena MSB ada di posisi terakhir)
    print("Nilai {} dari {} {} adalah {}.".format(tipe_tujuan, tipe_bilangan, angka_masukan, string_keluaran))


def operasi_ternary_septenary(angka):
    angka_keluaran = 0  # Inisiasi
    string_angka = str(angka)  # Agar bisa melakukan perkalian per digit
    for i in range(len(string_angka), 0, -1):
        angka_keluaran += (int(string_angka[i-1]) * (basis_bilangan**(len(string_angka) - i)))
        # Kalikan tiap digit dengan basis pangkat i, urutan dari LSB ke MSB
    if nomor_operasi == 2 or nomor_operasi == 4:
        # Jika hasil operasinya merupakan desimal, langsung keluarkan
        print("Nilai {} dari {} {} adalah {}.".format(tipe_tujuan, tipe_bilangan, angka_masukan, angka_keluaran))
    else:
        # Jika hasilnya lain, oper bilangan ke operasi desimal (karena sudah dikonversi ke desimal)
        operasi_decimal(angka_keluaran)


# Bagian Inti Program
print("---------------------------------------------")  # Demi estetika /uhuk/
print("Selamat datang di Program Konverter Bilangan!")

# Agar saat eksekusi operasi selesai, program dapat diulang tanpa harus dijalankan kembali
while True:
    # Bagian Pembuka
    print("---------------------------------------------")  # For sake of eye-candy display
    print("Menu:")
    print("   1. Decimal ke Ternary")
    print("   2. Ternary ke Decimal")
    print("   3. Decimal ke Septenary")
    print("   4. Septenary ke Decimal")
    print("   5. Ternary ke Septenary")
    print("   6. Septenary ke Ternary")
    print("   7. Keluar")
    print("---------------------------------------------")  # Iya iya, ini demi estetika (lagi)

    # Bagian Input Jenis Operasi
    try:
        nomor_operasi = int(input("Masukkan operasi yang ingin dilakukan: ​"))
    except ValueError:  # Apabila input bukan angka
        print("Maaf, input tidak valid.")
    else:
        # Handling Error Angka Input
        if nomor_operasi > 7 or nomor_operasi < 1:
            print("Maaf, input tidak valid.")
        # Handling Exit Program
        elif nomor_operasi == 7:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            # Handling Tipe Bilangan dan Basis Operasi
            if nomor_operasi == 1:
                tipe_bilangan = "decimal"
                tipe_tujuan = "ternary"
                basis_bilangan = 10
                basis_tujuan = 3
            elif nomor_operasi == 2:
                tipe_bilangan = "ternary"
                tipe_tujuan = "decimal"
                basis_bilangan = 3
                basis_tujuan = 10
            elif nomor_operasi == 3:
                tipe_bilangan = "decimal"
                tipe_tujuan = "septenary"
                basis_bilangan = 10
                basis_tujuan = 7
            elif nomor_operasi == 4:
                tipe_bilangan = "septenary"
                tipe_tujuan = "decimal"
                basis_bilangan = 7
                basis_tujuan = 10
            elif nomor_operasi == 5:
                tipe_bilangan = "ternary"
                tipe_tujuan = "septenary"
                basis_bilangan = 3
                basis_tujuan = 7
            elif nomor_operasi == 6:
                tipe_bilangan = "septenary"
                tipe_tujuan = "ternary"
                basis_bilangan = 7
                basis_tujuan = 3

            # Bagian Input
            try:
                angka = int(input("Masukkan angka yang ingin dikonversi: "))
            except ValueError:  # Apabila input bukan angka
                print("Input harus berupa angka {}!".format(tipe_bilangan))
            else:  # Jika lolos cek angka
                status_angka = True  # Nilai default
                # Handling Error Input secara Basis (khusus ternary dan septenary)
                if basis_bilangan == 3 or basis_bilangan == 7:
                    cek = str(angka)  # Agar bisa melakukan pengecekan per digit
                    for i in range(len(cek)):
                        if int(cek[i]) >= basis_bilangan:  # Apabila ada suatu digit yang melampaui basis bilangan
                            status_angka = False  # Angka tersebut tidak valid
                            print("Input harus berupa angka {}!".format(tipe_bilangan))
                            break
                if status_angka:  # Jika input angka tidak error
                    # Handling Angka ke Fungsi
                    angka_masukan = int(angka)
                    if nomor_operasi == 1 or nomor_operasi == 3:
                        operasi_decimal(angka_masukan)
                    else:
                        operasi_ternary_septenary(angka_masukan)

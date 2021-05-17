# Program: Average and Character Counter
# Program ini dibuat oleh Muhammad Athallah (2020)

# Sesuaikan dengan yang tertulis pada contoh interaksi
in_filename = input("Masukkan nama file input: ")
out_filename = input("Masukkan nama file output: ")

try:
    assert in_filename != out_filename
    """
    TODO - Task 1
     > Menerima Input
     > Membaca File
     > Menghitung total jumlah baris dan karakter pada file
     > Menghitung rata-rata jumlah karakter
     - Menulis output program ke dalam sebuah file dengan format .txt
    """
    # Tambahkan kode di bawah baris ini
    in_file = open(in_filename, "r")
    out_file = open(out_filename, "w")
    inputs = in_file.readlines()

    total_character = 0
    total_line = len(inputs)

    '''
    for line in inputs:
        for character in line:
            if character != "\n":
                total_character += 1
    '''
    for line in inputs:
        total_character += len(line) - 1  # Excluded "\n"
    outputs = total_character / total_line
    
    out_file.write(f"Terdapat {total_line} baris dan {total_character} karakter pada file {in_filename}\n")
    out_file.write(f"Rata-rata jumlah karakter dalam baris adalah {outputs:.2f} karakter\n")
    in_file.close()
    out_file.close()

except FileNotFoundError: # Diisi error handling file error
	print("File tidak ditemukan :(")

except AssertionError: # Diisi error handling nama file sama
	print("Nama file input harus berbeda dengan file output")

else: # Diisi statement yang dijalankan ketika program berjalan tanpa error
	print(f"Output berhasil ditulis pada {out_filename}")

input("Program selesai. Tekan enter untuk keluar...")

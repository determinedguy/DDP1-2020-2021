# Sesuaikan dengan yang tertulis pada contoh interaksi
in_filename = input(......)
out_filename = input(......)

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

except ......: # Diisi error handling file error
	print("File tidak ditemukan :(")

except ......: # Diisi error handling nama file sama
	print("Nama file input harus berbeda dengan file output")

......: # Diisi statement yang dijalankan ketika program berjalan tanpa error
	print(f"Output berhasil ditulis pada {out_filename}")

input("Program selesai. Tekan enter untuk keluar...")

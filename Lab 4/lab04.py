# Program: Min, Max, and Range of Character
# Program ini dibuat oleh Muhammad Athallah (2020)

# Sesuaikan dengan yang tertulis pada contoh interaksi
in_filename = input("Masukkan nama file: ")

try:
    # Tambahkan kode di bawah baris ini
    in_file = open(in_filename, "r+")
    inputs = in_file.readlines()

    min = 0
    max = 0
    input_first = False
    character = 0
    
    if inputs == []:
        in_file.write("NULL\n")
    else:
        for line in inputs:
            character = len(line) - 1  # Excluded "\n"
            if not input_first:
                min = character
                input_first = True
            if character > max:
                max = character
            elif character < min:
                min = character
    
        range = max - min

        in_file.write("########\n")
        in_file.write(f"Min: {min} karakter\n")
        in_file.write(f"Max: {max} karakter\n")
        in_file.write(f"Range: {range} karakter\n")
    
    in_file.close()

except FileNotFoundError: # Diisi error handling file error
	print("File tidak ditemukan :(")

else: # Diisi statement yang dijalankan ketika program berjalan tanpa error
	print(f"Output berhasil ditulis pada {in_filename}")

input("Program selesai. Tekan enter untuk keluar...")

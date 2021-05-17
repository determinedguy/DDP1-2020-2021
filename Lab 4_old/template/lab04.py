in_filename = input("Masukkan nama file input: ")
out_filename = input("Masukkan nama file output: ")

try:
    assert in_filename != out_filename # File input harus berbeda dengan file output

    total_char = 0
    total_line = 0
    with open(in_filename, "r") as in_file:
        for line in in_file:
            total_line += 1
            total_char += len(line) - 1 # -1 karena tidak menghitung karakter \n

    with open(out_filename, "w") as out_file:
        print(f"Terdapat {total_line} baris dan {total_char} karakter pada file {in_filename}", file=out_file)
        print(f"Rata-rata baris mengandung {total_char / total_line:.2f} karakter", file=out_file)

except FileNotFoundError:
	print("File tidak ditemukan :(")

except AssertionError:
	print("Nama file input harus berbeda dengan file output")

else:
    print(f"Output berhasil ditulis pada {out_filename}")

input("Program selesai. Tekan enter untuk keluar...")

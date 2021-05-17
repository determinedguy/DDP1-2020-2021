# Lab 7
# Program ini dibuat oleh Muhammad Athallah (2020)
# Program ini dibuat dengan diskusi bersama Sabyna Maharani dan Dinda Adriani Siregar

# Fungsi ini menggabungkan seluruh string dalam tuple menjadi satu string
def remove_to_str(str_tup):
    # Cek apakah tipe datanya (masih) tuple
    if isinstance(str_tup, tuple):
        # Apabila isi tuplenya kosong
        if len(str_tup) == 0:
            # Maka kembalikan spasi [KASUS #0]
            return ''
        # Apabila panjang tuplenya 1
        elif len(str_tup) == 1:
            # Apabila isi tuplenya merupakan tuple (tuple dalam tuple)
            if isinstance(str_tup[0], tuple):
                # Maka gunakan rekursi pada tuple [KASUS #1]
                return remove_to_str(str_tup[0])
            # Apabila isi tuplenya merupakan string (selain tuple)
            else:
                # Maka kembalikan isi string [KASUS #2]
                return str_tup[0]
        # Apabila panjang tuplenya lebih dari 1
        else:
            # Maka pecah menjadi dua kasus rekursi [KASUS #3]
            return (remove_to_str(str_tup[0])) + ' ' + (remove_to_str(str_tup[1:]))
    # Apabila tipe datanya string (selain tuple)
    else:
        # Maka kembalikan isi string [KASUS #4]
        return str_tup
    
# Menggunakan eval() untuk mengubah input (dengan tipe data str) menjadi tuple
string_tuple = eval(input())
# Masukkan ke dalam fungsi rekursi
string_gabung = remove_to_str(string_tuple)
# Cek apakah string yang dikembalikan tidak kosong (hanya spasi)
if string_gabung:

    # Pecah string menjadi list (untuk menghilangkan spasi dan spasi berlebih (dari KASUS #0))
    list_result = string_gabung.split()
    # Gabungkan list menjadi satu string dan cetak
    string_total = " ".join(list_result)
    print(string_total)

    # Perbaikan dari list menjadi set untuk memenuhi [CHALLENGE]
    list_result = set(string_gabung.split())
    # Gabungkan set menjadi satu string dan cetak
    string_total = " ".join(list_result)
    print(string_total)

# Apabila string merupakan string kosong, maka kembalikan "kosong"
else:
    print("kosong")
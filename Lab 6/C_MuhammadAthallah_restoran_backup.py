# meminta masukan jumlah donat
jumlah_donat = int(input("Masukkan Jumlah Donat DUAARRR!!!: "))
# inisiasi dictionary untuk data donat dengan nama
data_donat_nama = dict()
# inisiasi (apaan?) untuk data donat dengan rasa
# tidak bisa memakai dictionary karena kemungkinan rasa sama, harga beda
data_donat_rasa = {}
# mengambil data donat
for i in range(jumlah_donat):
    print(f"Data {i+1}: ", end = '')
    nama, harga, rasa = input().split()
    # memasukkan data harga pada dictionary
    data_donat_nama[nama] = int(harga)
    data_donat_rasa[rasa] = int(harga)
print()
# meminta masukan jumlah pembeli
jumlah_pembeli = int(input("Masukkan Jumlah Pembeli: "))
# inisiasi data penjualan
donat_terjual = set()
uang_pendapatan = 0
# mengambil data pembeli
for i in range(jumlah_pembeli):
    print(f"Pembeli {i+1}: ", end = '')
    perintah, barang = input().split()
    # bagi menjadi dua kasus, kasus nama dan kasus rasa
    if perintah == "BELI_NAMA":
        # apabila ditemukan
        if barang in data_donat_nama:
            keluaran_harga = data_donat_nama[barang]
            print(f"{barang} terjual dengan harga {keluaran_harga}")
            # tambahkan data penjualan
            donat_terjual.add(barang)
            uang_pendapatan += keluaran_harga
        else:
            print(f"Tidak ada Donat DUAARRR!!! dengan nama {barang} :(")
    # dengan asumsi tidak ada input selain nama dan rasa
    else:
        if barang in data_donat_rasa:
            continue
        else:
            print(f"Tidak ada Donat DUAARRR!!! dengan rasa {barang} :(")
print()
# kumpulkan nama-nama donat yang terjual ke dalam satu string
donat_terjual_string = ', '.join(donat_terjual)
# keluarkan data donat yang terjual
print(f"Donat Terjual: {donat_terjual_string}")
# keluarkan pendapatan
print(f"Total Pendapatan: {uang_pendapatan}")
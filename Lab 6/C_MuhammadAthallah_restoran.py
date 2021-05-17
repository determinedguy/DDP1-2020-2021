# meminta masukan jumlah donat
jumlah_donat = int(input("Masukkan Jumlah Donat DUAARRR!!!: "))
# inisiasi dictionary untuk data donat dengan nama
data_donat_nama = dict()
# inisiasi dictionary untuk data donat dengan rasa
data_donat_rasa = {}
# mengambil data donat
for i in range(jumlah_donat):
    print(f"Data {i+1}: ", end = '')
    nama, harga, rasa = input().split()
    # memasukkan data harga pada dictionary dengan dasar nama donat
    data_donat_nama[nama] = int(harga)
    # mengecek apakah sudah ada rasa dalam data_donat_rasa
    # jika belum, maka inisiasi list kosong
    if not (rasa in data_donat_rasa):
        data_donat_rasa[rasa] = []
    # memasukkan data harga berupa tuples pada dictionary rasa
    # variabel temp akan menginisiasi tuple berisi dua item
    # contoh: (2000, DonatCP)
    temp = int(harga), nama
    data_donat_rasa[rasa].append(temp)
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
        # apabila ditemukan key nama pada dictionary
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
        # apabila ditemukan key rasa pada dictionary
        if barang in data_donat_rasa:
            # ambil list of tuples berupa isi dari rasa yang dipilih
            data_tetapan = data_donat_rasa[barang]
            # sort untuk mendapatkan harga tertinggi di akhir indeks
            data_tetapan.sort(key=lambda x: x[0])
            # ambil data terakhir untuk mendapatkan harga tertinggi
            keluaran_harga = data_tetapan[-1][0]
            keluaran_donat = data_tetapan[-1][1]
            # keluarkan output
            print(f"{keluaran_donat} terjual dengan harga {keluaran_harga}")
            # tambahkan data penjualan
            donat_terjual.add(keluaran_donat)
            uang_pendapatan += keluaran_harga
        else:
            print(f"Tidak ada Donat DUAARRR!!! dengan rasa {barang} :(")
print()
# kumpulkan nama-nama donat yang terjual ke dalam satu string
donat_terjual_string = ', '.join(donat_terjual)
# keluarkan data donat yang terjual
print(f"Donat Terjual: {donat_terjual_string}")
# keluarkan pendapatan
print(f"Total Pendapatan: {uang_pendapatan}")

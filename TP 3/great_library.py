# Tugas Pemrograman 3: The Great Library
# Dibuat oleh Muhammad Athallah (2020)

# Inisiasi variabel global
pustaka = {}

# Fungsi SEARCH, menggunakan implementasi recursive linear search
# Sumber: https://www.geeksforgeeks.org/recursive-c-program-linearly-search-element-given-array/
# Mengembalikan indeks dari buku yang dicari (apabila ada)
# Jika tidak ada, maka kembalikan nilai -1
def recursive_search(arr, l, r, x):
    # Apabila batas kanan lebih besar daripada batas kiri (invalid/out of index)
    if r < l:
        return -1
    # Apabila list dengan indeks batas kiri berisi buku yang dicari
    if arr[l][0] == x:
        return l
    # Apabila list dengan indeks batas kanan berisi buku yang dicari
    if arr[r][0] == x:
        return r
    # Apabila belum ditemukan buku (rekursi kembali)
    return recursive_search(arr, l+1, r-1, x)

def mechanism_search(rak_buku, cari, i = 0):
    # Inisiasi variabel
    indeks = -1
    # Inisiasi key dari variabel pustaka (berisi nama-nama rak)
    tiap_rak = tuple(rak_buku.keys())
    # Selama masih ada rak, eksekusi
    if i < len(tiap_rak):
        daftar_buku = rak_buku[tiap_rak[i]] # Berisi list of tuples
        batas_kiri = 0
        batas_kanan = len(daftar_buku)-1
        buku = cari
        indeks = recursive_search(daftar_buku, batas_kiri, batas_kanan, buku)
        # Apabila buku ditemukan, langsung kembalikan indeks dan rak dari lokasi buku
        if indeks != -1:
            return [indeks, tiap_rak[i]]
        # Jika belum, maka ulangi proses (rekursi)
        else:
            return mechanism_search(rak_buku, cari, i+1)
    # Jika semua rak telah diperiksa dan buku tidak ditemukan
    return [-1, -1]

def search(rak, perintah):
    # Mengecek apakah perintah valid
    if len(perintah) != 3 or perintah[1] != "BUKU":
        print("Perintah tidak valid")
        # Menghentikan fungsi (alternatif dari if-else)
        return 0
        
    # Dilakukan pencarian dalam tiap rak buku
    list_cari = mechanism_search(rak, perintah[2])
    indeks_cari = list_cari[0]
    kunci_rak = list_cari[1]

    # Apabila buku ditemukan
    if indeks_cari != -1:
        print("Buku ditemukan")
        print(f"Nama buku: {pustaka[kunci_rak][indeks_cari][0]}")
        print(f"Posisi: {kunci_rak}")
        print(f"Pengarang: {pustaka[kunci_rak][indeks_cari][1]}")
        print(f"Tahun Terbit: {pustaka[kunci_rak][indeks_cari][2]}")
        print(f"Penerbit: {pustaka[kunci_rak][indeks_cari][3]}")
        print(f"Genre: {pustaka[kunci_rak][indeks_cari][4]}")
    else:
        print("Buku tidak ditemukan")


# Fungsi ADD
def add(perintah):
    # Menggunakan prinsip legb
    global pustaka

    # Subfungsi ADD RAK
    if perintah[1] == "RAK":
        # Mengecek apakah perintah valid
        if len(perintah) != 3:
            print("Perintah tidak valid")
            # Menghentikan fungsi (alternatif dari if-else)
            return 0

        kunci_rak = perintah[2]
        # Mengecek apakah nama rak sudah ada
        if kunci_rak in pustaka:
            print(f"Rak dengan nama {kunci_rak} sudah ada di dalam sistem")
        # Tambahkan jika belum
        else:
            # Inisiasi list of tuples
            # Judul buku akan menjadi key dari masing-masing dict
            pustaka[kunci_rak] = []
            print(f"Rak dengan nama {kunci_rak} berhasil ditambahkan")
    
    # Subfungsi ADD BUKU
    elif perintah[1] == "BUKU":

        """
        Bug: Cek buku dulu, baru rak
        """
        # Mengecek apakah perintah valid
        if len(perintah) != 8:
            print("Perintah tidak valid")
            # Menghentikan fungsi (alternatif dari if-else)
            return 0
        
        nama_rak = perintah[2]
        nama_buku = perintah[3]
        penulis = perintah[4]
        tahun = perintah[5]
        penerbit = perintah[6]
        genre = perintah[7]

        # Mengecek apakah nama buku sudah ada pada rak
        list_cari = mechanism_search(pustaka, nama_buku)
        indeks_cari = list_cari[0]

        # Jika buku sudah ada pada rak
        if indeks_cari != -1:
            print(f"Buku dengan nama {nama_buku} sudah ada di dalam sistem")

        else:
            # Jika buku tidak ada (baru) namun rak belum diinisiasi
            if not (nama_rak in pustaka):
                # Inisiasi rak baru berupa list of tuples
                # Judul buku akan menjadi key dari masing-masing dict
                pustaka[nama_rak] = []
                print(f"Rak dengan nama {nama_rak} berhasil ditambahkan")

            # Inisiasi data buku berupa tuple
            pustaka[nama_rak].append((nama_buku, penulis, tahun, penerbit, genre))
            print(f"Buku dengan nama {nama_buku}, {tahun}, {penerbit}, {genre} berhasil ditambahkan")

    else:
        print("Perintah tidak valid")


# Fungsi MOVE
def move(perintah):
    # Menggunakan prinsip legb
    global pustaka

    # Mengecek apakah perintah valid
    if len(perintah) != 4 or perintah[1] != "BUKU":
        print("Perintah tidak valid")
        # Menghentikan fungsi (alternatif dari if-else)
        return 0
    
    nama_buku = perintah[2]
    rak_tujuan = perintah[3]

    # Jika buku tidak ada (baru) namun rak belum diinisiasi
    if not rak_tujuan in pustaka:
        # Inisiasi rak baru berupa list of tuples
        # Judul buku akan menjadi key dari masing-masing dict
        pustaka[rak_tujuan] = []
        print(f"Rak dengan nama {rak_tujuan} berhasil ditambahkan")
    
    # Mengecek posisi buku pada rak
    list_cari = mechanism_search(pustaka, perintah[2])
    indeks_cari = list_cari[0]
    rak_asal = list_cari[1]

    # Apabila buku tidak ditemukan
    if indeks_cari == -1:
        print("Buku tidak ditemukan")
    else:
        pustaka[rak_tujuan].append(pustaka[rak_asal][indeks_cari])
        pustaka[rak_asal].remove(pustaka[rak_asal][indeks_cari])
        print(f"Buku dengan nama {nama_buku} dipindahkan dari rak dengan nama {rak_asal} ke rak dengan nama {rak_tujuan}")

# Bagian utama program
while True:
    print("Selamat datang di The Great Library")
    print("Silakan masukkan perintah!")
    # Masukan akan ditampung pada tipe data string
    masukan_perintah = input("Perintah anda: ")
    # Perintah dipecah menjadi sebuah list of substrings
    list_perintah = masukan_perintah.split()

    # Bagian pecah perintah
    if list_perintah[0] == 'ADD':
        add(list_perintah)
    elif list_perintah[0] == 'MOVE':
        move(list_perintah)
    elif list_perintah[0] == 'SEARCH':
        search(pustaka, list_perintah)
    elif list_perintah[0] == 'EXIT':
        print("Selesai, sistem dimatikan")
        break
    else:
        print("Perintah tidak dikenali")
    print()
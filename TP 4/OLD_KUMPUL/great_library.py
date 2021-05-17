# Tugas Pemrograman 4 [FINALE]: The Great Library, part 2
# Program ini dibuat oleh Muhammad Athallah (2020)

class Book:

    def __init__(self, nama, tahun, pengarang, penerbit):
        """
        Constructor untuk class Book
        """
        self.__nama = nama
        self.__tahun = tahun
        self.__pengarang = pengarang
        self.__penerbit = penerbit
    
    # Getter
    def get_book_description(self):
        """
        Getter untuk mencetak deskripsi buku
        """
        print(f"Nama Buku: {self.__nama}")
        print(f"Tahun: {self.__tahun}")
        print(f"Pengarang: {self.__pengarang}")
        print(f"Penerbit: {self.__penerbit}")

    def __str__(self):
        return self.__nama
    
    # Bagian Komparasi

    # Membandingkan nama dari masing-masing buku untuk pengurutan secara ASCIIbetical order [LIST]
    def __lt__(self, other):
        return self.__nama < other.__nama
    
    # Membandingkan judul buku dengan nama buku yang dicari untuk pencarian buku [SEARCH]
    def __eq__(self, other):
        return self.__nama == other


class FictionBook(Book):
    
    def __init__(self, nama, tahun, pengarang, penerbit, genre):
        """
        Constructor untuk class FictionBook
        """
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__genre = genre
    
    # Getter
    def get_book_description(self):
        """
        Getter untuk mencetak deskripsi buku
        """
        # Referensi: https://www.geeksforgeeks.org/method-overriding-in-python/
        # Bisa menggunakan Class.method() atau super().method()
        print("Buku Fiksi")
        super().get_book_description() # atau Book.get_book_description(self) 
        print(f"Genre: {self.__genre}")


class ReferenceBook(Book):
    
    def __init__(self, nama, tahun, pengarang, penerbit, kota_terbit):
        """
        Constructor untuk class ReferenceBook
        """
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__kota_terbit = kota_terbit
    
    # Getter
    def get_book_description(self):
        """
        Getter untuk mencetak deskripsi buku
        """
        print("Buku Referensi")
        super().get_book_description()
        print(f"Kota Penerbit: {self.__kota_terbit}")


class Encyclopedia(Book):
    
    def __init__(self, nama, tahun, pengarang, penerbit, revisi_num):
        """
        Constructor untuk class EncyclopediaBook
        """
        super().__init__(nama, tahun, pengarang, penerbit)
        self.__revisi_num = revisi_num
    
    # Getter
    def get_book_description(self):
        """
        Getter untuk mencetak deskripsi buku
        """
        print("Buku Ensiklopedia")
        super().get_book_description()
        print(f"Revisi ke: {self.__revisi_num}")


class Shelf:

    def __init__(self, nama, kumpulan_buku):
        """
        Constructor untuk class Shelf
        """
        self.__nama = nama
        self.__kumpulan_buku = kumpulan_buku
    
    def search_buku(self, buku):
        """
        Mencari keberadaan buku dalam tiap rak.
        Apabila ditemukan, maka kembalikan indeks buku.
        Jika tidak, maka kembalikan -1.
        """
        # Untuk setiap objek buku dalam rak
        for i in range(len(self.get_buku())):
            # Apabila ditemukan (menggunakan __eq__), kembalikan indeks
            if buku == self.get_buku()[i]:
                return i
        
        return -1

    # Setter
    def set_buku(self, isi):
        """
        Inisiasi buku ke dalam list
        """
        self.__kumpulan_buku.append(isi)

    # Getter
    def get_buku(self):
        """
        Getter dari list objek-objek buku
        """
        return self.__kumpulan_buku
    
    def list_buku(self):
        """
        Getter untuk daftar buku
        """
        # Akses list dari objek-objek buku per rak
        buku_dalam_rak = self.get_buku()
        # Urutkan berdasarkan judul (menggunakan __lt__)
        buku_dalam_rak.sort()
        # Untuk setiap buku dalam rak
        for buku in buku_dalam_rak:
            print(f"   -  {buku}")


class KnowledgeShelf(Shelf):
    
    def __init__(self, nama, kumpulan_buku):
        """
        Constructor untuk class KnowledgeShelf
        """
        super().__init__(nama,kumpulan_buku)
    
    # Setter
    def add_buku(self, isi):
        """
        Menambahkan buku dalam rak
        """
        nama, tahun, pengarang, penerbit, jenis, atribut = isi
        if jenis == "Ensiklopedia":
            buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        elif jenis == "Referensi":
            buku = ReferenceBook(nama, tahun, pengarang, penerbit, atribut)
        
        self.set_buku(buku)


class WorldShelf(Shelf):
    
    def __init__(self, nama, kumpulan_buku):
        """
        Constructor untuk class WorldShelf
        """
        super().__init__(nama,kumpulan_buku)
    
    # Setter
    def add_buku(self, isi):
        """
        Menambahkan buku dalam rak
        """
        nama, tahun, pengarang, penerbit, jenis, atribut = isi
        if jenis == "Fiksi":
            buku = FictionBook(nama, tahun, pengarang, penerbit, atribut)
        elif jenis == "Ensiklopedia":
            buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        
        self.set_buku(buku)


class MysteryShelf(Shelf):
    
    def __init__(self, nama, kumpulan_buku):
        """
        Constructor untuk class MysteryShelf
        """
        super().__init__(nama,kumpulan_buku)
    
    # Setter
    def add_buku(self, isi):
        """
        Menambahkan buku dalam rak
        """
        nama, tahun, pengarang, penerbit, jenis, atribut = isi
        if jenis == "Fiksi":
            buku = FictionBook(nama, tahun, pengarang, penerbit, atribut)
        elif jenis == "Referensi":
            buku = ReferenceBook(nama, tahun, pengarang, penerbit, atribut)
        
        self.set_buku(buku)


class CompendiumShelf(Shelf):

    def __init__(self, nama, kumpulan_buku):
        """
        Constructor untuk class CompendiumShelf
        """
        super().__init__(nama,kumpulan_buku)
    
    # Setter
    def add_buku(self, isi):
        """
        Menambahkan buku dalam rak
        """
        nama, tahun, pengarang, penerbit, jenis, atribut = isi
        if jenis == "Fiksi":
            buku = FictionBook(nama, tahun, pengarang, penerbit, atribut)
        elif jenis == "Ensiklopedia":
            buku = Encyclopedia(nama, tahun, pengarang, penerbit, atribut)
        elif jenis == "Referensi":
            buku = ReferenceBook(nama, tahun, pengarang, penerbit, atribut)
                    
        self.set_buku(buku)


class Library:

    def __init__(self, kumpulan_rak):
        """
        Constructor untuk class Library
        """
        self.__kumpulan_rak = kumpulan_rak
    
    def search_rak(self, nama):
        """
        Mencari keberadaan rak dalam perpustakaan.
        Mengembalikan 1 (TRUE) jika ada, 0 (FALSE) apabila sebaliknya.
        """
        if nama in self.get_rak():
            return 1
        else:
            return 0

    def search_buku(self, nama):
        """
        Mencari keberadaan buku dalam perpustakaan.
        Memanggil search_buku pada class Shelf untuk tiap rak.
        Apabila ditemukan, maka method akan dihentikan.
        Apabila tidak ditemukan, pesan akan dicetak.
        """
        # Inisiasi status penemuan buku
        status = False

        # Untuk setiap rak dalam perpustakaan
        for rak in self.get_rak():
            # Akses list dari rak, berisi objek-objek buku
            isi_rak = self.get_rak()[rak]
            # Panggil method per rak
            index = isi_rak.search_buku(nama)
            if index != -1:
                print("Buku ditemukan\n")
                isi_rak.get_buku()[index].get_book_description()
                status = True
                break
        
        if not status:
            print(f"Buku dengan nama {nama} tidak ditemukan")

    # Getter
    def get_rak(self):
        return self.__kumpulan_rak
    
    # Setter
    def add_rak(self, jenis, nama):
        """
        Menambahkan rak dalam perpustakaan
        """
        # Memisahkan per jenis rak
        if jenis == "Pengetahuan":
            rak = KnowledgeShelf(nama, [])
        elif jenis == "Dunia":
            rak = WorldShelf(nama, [])
        elif jenis == "Misteri":
            rak = MysteryShelf(nama, [])
        elif jenis == "Compendium":
            rak = CompendiumShelf(nama, [])

        # Masukkan rak dalam perpustakaan
        self.__kumpulan_rak[nama] = rak

    def add_buku(self, rak, daftar_perintah):
        """
        Menambahkan buku ke dalam rak, akan dibagi sesuai spesifikasi rak tujuan.
        Apabila buku berhasil ditambahkan, kembalikan TRUE.
        Jika tidak, maka kembalikan FALSE.
        """
        # Inisiasi variabel
        jenis = daftar_perintah[4]
        nama_buku = daftar_perintah[0]
        success = False
        perintah_gagal = "Buku gagal ditambahkan :("

        # Jika rak ditemukan
        if self.search_rak(rak):
        
            # Mengecek jenis rak dan buku masing-masing
            if isinstance(self.__kumpulan_rak[rak], KnowledgeShelf):
                if jenis in ("Ensiklopedia", "Referensi"):
                    self.__kumpulan_rak[rak].add_buku(daftar_perintah)
                    success = True
                else:
                    print(perintah_gagal)
            
            elif isinstance(self.__kumpulan_rak[rak], WorldShelf):
                if jenis in ("Ensiklopedia", "Fiksi"):
                    self.__kumpulan_rak[rak].add_buku(daftar_perintah)
                    success = True
                else:
                    print(perintah_gagal)
            
            elif isinstance(self.__kumpulan_rak[rak], MysteryShelf):
                if jenis in ("Fiksi", "Referensi"):
                    self.__kumpulan_rak[rak].add_buku(daftar_perintah)
                    success = True
                else:
                    print(perintah_gagal)
            
            elif isinstance(self.__kumpulan_rak[rak], CompendiumShelf):
                if jenis in ("Ensiklopedia", "Referensi", "Fiksi"):
                    self.__kumpulan_rak[rak].add_buku(daftar_perintah)
                    success = True
                else:
                    print(perintah_gagal)
            
            else:
                print(perintah_gagal)
            
            # Jika operasi berhasil dijalankan
            if success:
                print(f"Buku baru berhasil ditambahkan pada {rak}")
                print()
                # Mencari kembali indeks buku pada rak, kemudian cetak deskripsi buku
                index = self.get_rak()[rak].search_buku(nama_buku)
                self.get_rak()[rak].get_buku()[index].get_book_description()
                return True
        
        else:
            print(perintah_gagal)
        
        return False

    def list_buku(self):
        """
        Getter untuk daftar rak, getter untuk daftar buku akan dihandle dalam tiap rak.
        """
        rak = self.get_rak()
        # Untuk setiap rak dalam perpustakaan
        for nama_rak in rak:
            # Cetak nama rak, kemudian akses list_buku() per rak
            print(nama_rak)
            rak[nama_rak].list_buku()


def main():
    # Inisiasi perpustakaan
    pustaka = Library({})
    # Tambahkan rak-rak default
    pustaka.add_rak("Pengetahuan", "Pengetahuan01")
    pustaka.add_rak("Dunia", "Dunia01")
    pustaka.add_rak("Misteri", "Misteri01")
    pustaka.add_rak("Compendium", "Compendium01")
    # Inisiasi status "apakah sudah ada buku yang ditambahkan" (untuk LIST)
    any_book = False
    # Inisiasi variabel pembantu
    perintah_invalid = "Perintah tidak valid"
    perintah_tidak_dikenali = "Perintah tidak dikenali"
    daftar_rak_valid = ("Pengetahuan", "Dunia", "Misteri", "Compendium")

    while True:
        print("Selamat datang di The Great Library")
        print("Silakan masukkan perintah!")
        command = ""
        # Selama belum menerima masukan, minta masukan
        while not command:
            command = input("Perintah anda: ").split()
        
        if command[0] == "EXIT":
            print("Selesai, Sistem dimatikan.")
            break
        
        elif command[0] == "ADD":
            if command[1] == "RAK":
                if len(command) != 4:
                    print(perintah_invalid)
                else:
                    nama_rak = command[2]
                    jenis_rak = command[3]
                    # Mengecek apakah rak dengan nama_rak sudah ada
                    if pustaka.search_rak(nama_rak):
                        print(f"Rak dengan nama {nama_rak} sudah ada di dalam sistem")
                    # Mengecek apakah jenis rak termasuk ke jenis rak yang valid
                    elif jenis_rak in daftar_rak_valid:
                        pustaka.add_rak(jenis_rak, nama_rak)
                        print("Rak baru berhasil ditambahkan\n")
                        print(f"Nama: {nama_rak}")
                        print(f"Jenis: {jenis_rak}")
                    else:
                        print(perintah_invalid)
            
            elif command[1] == "BUKU":
                if len(command) != 9:
                    print(perintah_invalid)
                else:
                    # Slicing perintah dan masukkan ke method, tunggu hasil dari method
                    nama_rak = command[2]
                    perintah = command[3:]
                    status = pustaka.add_buku(nama_rak, perintah)
                    # Apakah buku sukses ditambahkan?
                    # Jika sukses, maka ubah status (untuk LIST)
                    if status:
                        any_book = True
        
        elif command[0] == "SEARCH":
            if len(command) != 2:
                print(perintah_invalid)
            else:
                nama_buku = command[1]
                pustaka.search_buku(nama_buku)
        
        elif command[0] == "LIST":
            # Jika sudah ada buku yang ditambahkan
            if any_book:
                print()
                pustaka.list_buku()
            # Jika belum ada buku yang ditambahkan
            else:
                print("Belum ada buku di dalam sistem :(")
        
        else:
            print(perintah_tidak_dikenali)
        
        print()


if __name__ == "__main__":
    main()

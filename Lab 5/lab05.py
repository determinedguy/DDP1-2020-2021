# Nama Program: Keranjang Boba
# Program ini dibuat oleh Muhammad Athallah (2020)
# Template digunakan dalam kode ini

# List daftar_keranjang untuk menyimpan semua keranjang
daftar_keranjang = []

def beli_keranjang(nama_keranjang, kapasitas_keranjang):
	'''
		Implementasikan fungsi untuk menambahkan
		keranjang dengan nama 'nama_keranjang'
		dan kapasitas 'kapasitas_keranjang'
	'''
	daftar_keranjang.append([nama_keranjang, kapasitas_keranjang])
	print(f"Berhasil menambahkan {nama_keranjang} dengan kapasitas {kapasitas_keranjang}.")
	pass

def jual_keranjang(indeks):
	'''
		Implementasikan fungsi untuk menghapus
		keranjang dengan index 'indeks'
	'''
	indeks = int(indeks)
	print(f"Berhasil menjual {daftar_keranjang[indeks][0]} yang memiliki kapasitas sebesar {daftar_keranjang[indeks][1]}.")
	daftar_keranjang.pop(indeks)
	pass

def ubah_kapasitas(indeks, kapasitas_baru):
	'''
		Implementasikan fungsi untuk mengubah kapasitas
		keranjang dengan index 'indeks' menjadi 'kapasitas_baru'
	'''
	indeks = int(indeks)
	daftar_keranjang[indeks][1] = kapasitas_baru
	print(f"Berhasil mengubah kapasitas {daftar_keranjang[indeks][0]} menjadi {kapasitas_baru}.")
	pass

def ubah_nama(indeks, nama_baru):
	'''
		Implementasikan fungsi untuk mengubah nama
		keranjang dengan index 'indeks' menjadi 'nama_baru'
	'''
	indeks = int(indeks)
	print(f"Berhasil mengubah nama {daftar_keranjang[indeks][0]} menjadi {nama_baru}.")
	daftar_keranjang[indeks][0] = nama_baru
	pass

def lihat(indeks):
	'''
		Implementasikan fungsi untuk mencetak informasi
		keranjang dengan index 'indeks'
	'''
	indeks = int(indeks)
	print(f"Keranjang {daftar_keranjang[indeks][0]} memiliki kapasitas sebesar {daftar_keranjang[indeks][1]}.")
	pass

def lihat_semua():
	'''
		Implementasikan fungsi untuk mencetak semua 
		keranjang dalam bentuk table
	'''
	print("Keranjang Dek Depe")
	print("-"*30)
	for indeks in daftar_keranjang:
		print(indeks[0] + (" " * (24 - len(indeks[0])) + "|" + indeks[1]))
	pass

def total_kapasitas():
	'''
		Implementasikan fungsi yang mereturn
		sebuah integer yang menyatakan
		total kapasitas keranjang yang dimiliki Dek Depe
	'''
	total = 0
	for indeks in daftar_keranjang:
		total += int(indeks[1])
	print(f"Total kapasitas keranjang Dek Depe adalah ​{total}.")
	return 0


'''
Baris-baris program di bawah ini adalah main program dari program ini.
'''
jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
	operasi = input(f"\nMasukkan operasi {i+1}: ")	# Input query sebagai 1 string
	
	# Pecah operasi menggunakan method .split() dan tampung ke sebuah variable
	list_operasi = operasi.split()
	operasi = list_operasi[0]

	if (operasi == "BELI"):
		beli_keranjang(list_operasi[1], list_operasi[2])
		pass
	elif (operasi == "JUAL"):
		jual_keranjang(list_operasi[1])
		pass
	elif (operasi == "UBAH_KAPASITAS"):
		ubah_kapasitas(list_operasi[1], list_operasi[2])
		pass
	elif (operasi == "UBAH_NAMA"):
		ubah_nama(list_operasi[1], list_operasi[2])
		pass
	elif (operasi == "LIHAT"):
		lihat(list_operasi[1])
		pass
	elif (operasi == "LIHAT_SEMUA"):
		lihat_semua()
		pass
	else:
		total_kapasitas()
		pass

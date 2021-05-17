# Program: Berpacu Dalam Lirik
# Program ini dibuat oleh Muhammad Athallah (2020)

import os, random

# Fungsi di bawah dimanfaatkan untuk memulai permainan. 
# Mengembalikan tuple (string, string, int, int, list)
#     string pemain - nama pemain yang dijamin sudah valid
#     string mode   - Game Mode yang dipilih pemain
#     int score     - skor awal pemain, mulai dari 0
#     int nyawa     - kesempatan bermain pemain, tergantung Game Mode yang dipilih
#     list lagu     - list berisi semua nama file dalam folder lagu

def start_game():
    print("""
  _                                      
 | |__   ___ _ __ _ __   __ _  ___ _   _ 
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝ 
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗ 
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝                              
  """)
    print("~"*50)
    pemain = input("masukkan username     : ")
    mode = ''
    score = 0
    nyawa = 0
    lagu =  os.listdir("lagu")

    while pemain == "null" or pemain == "" or pemain == "NULL":
        pemain = input("harap gunakan nama yang valid.\nmasukkan username     : ")
    while mode.lower() not in ["normal", "expert"]:
        mode = input("mode (normal/expert)  : ")    

    if mode.lower() == "normal":
        nyawa = 3
    else:
        nyawa = 1

    print("~"*50)
    print("Good Luck & Have Fun :)\n")
    return pemain, mode, score, nyawa, lagu

# Fungsi di bawah membuka file dalam folder sesuai nama file lagu yang terpilih.
# Mengembalikan sebuah list isi file {nama_file}.txt 
def generate_lagu(nama_file): 
    with open(f"lagu/{nama_file}", 'r') as lagu_terpilih:
        lirik = lagu_terpilih.readlines()
    return lirik

# Fungsi di bawah memilih lirik lagu yang akan ditanya secara acak.
# Lirik lagu yang dikeluarkan harus didahului oleh empat bait sebelumnya.
# Mengembalikan indeks lirik yang terpilih
def generate_lirik(lirik_lagu):
  index = random.randint(4, len(lirik_lagu)-1)
  return index

# Fungsi di bawah memilih lagu yang akan ditanya secara acak.
# Lagu yang telah dipilih di ronde sebelumnya tidak akan terpilih selanjutnya.
# Mengembalikan judul lagu yang terpilih
def generate_judul(lagu):
  lagu_terpilih = random.choice(lagu)
  lagu.remove(lagu_terpilih)
  return lagu_terpilih

# Fungsi di bawah memeriksa apakah file highscore.txt sudah ada di directory,
# serta mengembalikan file stream highscore.txt yang telah dibuka
# Parameter:
#     purpose 'read' / 'replace' - tujuan membuka file highscore.txt
# Mengembalikan file stream highscore.txt
def get_highscore_or_create(purpose): 
    hs = os.listdir()
    highscore = None
    # check if doesn't exist, then create default 
    if "highscore.txt" not in hs:
        highscore = open("highscore.txt", 'w')
        a = ["normal null 0\n", "expert null 0\n"]
        highscore.writelines(a)

    # opens highscore.txt in desired mode
    if purpose == 'read': 
        highscore = open("highscore.txt", 'r')
    else: 
        highscore = open("highscore.txt", 'w')
    return highscore

# Fungsi di bawah merupakan fungsi inti game
def game_on(score, nyawa):
  # Set status penyelesaian ronde game secara sempurna menjadi False
  finished = False
  # Satu game terdiri dari lima babak
  for i in range(5):
    # Jika nyawa sudah habis, maka berhenti
    if nyawa == 0:
      break
    else:
      print(f"Round {i+1}")
      print(f"Nyawa : {nyawa}")
      print(f"Score : {score}")
      print("~"*50)
      # Melakukan pemilihan secara acak
      judul = generate_judul(lagu)
      lirik = generate_lagu(judul)
      indeks = generate_lirik(lirik)
      print(f"Judul lagu : {judul.replace('.txt', '')}")
      for clue in range (indeks - 4, indeks):
        print(lirik[clue], end='')
      # Melakukan operasi untuk lirik yang ditebak
      lirik_tebakan = ""
      for karakter in lirik[indeks]:
        # Untuk menghilangkan '\n' agar tidak salah saat comparison
        if karakter != '\n':
          lirik_tebakan += karakter
      print("Silakan menebak:")
      tebakan = input()
      # Whitespace setelah jawaban masih tetap dihitung benar, namun tidak dihitung sebagai skor
      # Revisi 23 Oktober 2020
      # Memakai method strip() untuk menghilangkan leading and trailing whitespaces
      tebakan = tebakan.strip()
      # Pengecekan kesamaan, memakai method lower()
      # print(lirik_tebakan)
      # print(tebakan)
      if (lirik_tebakan.lower() == tebakan.lower()):
        print("Jawaban BENAR\n")
        score += len(lirik_tebakan) - 1
        # Jika kelima ronde diselesaikan secara sempurna, maka berikan tanda
        if (i == 4):
          finished = True
      else:
        print("Jawaban SALAH")
        print(f"Jawaban : {lirik_tebakan}\n")
        nyawa -= 1
  # Jika kelima ronde diselesaikan secara sempurna, maka berikan selamat
  if finished:
    print("SELAMAT!")
    print("Anda berhasil menyelesaikan permainan.\n")
    print("Hasil Akhir:")
    print(f"Score: {score}\n")
  else:
    print("GAME OVER")
    print(f"Sayang sekali {pemain}, Anda terhenti disini.\n")
    print("Hasil Akhir:")
    print(f"Score: {score}\n")
  return score

# Fungsi di bawah merupakan fungsi pencetak skor
def highscore_part(pemain, mode, score):
  # Bagian Read File
  highscore = get_highscore_or_create('read')
  score_part = highscore.readlines()
  highscore.close()
  # Set fungsi file menjadi writable
  highscore = get_highscore_or_create('replace')
  # Bagian Pemecahan Lines menjadi String
  list_normal = score_part[0].split()
  list_expert = score_part[1].split()
  # Ambil nilai dari string masing-masing
  normal_score = int(list_normal[len(list_normal)-1])
  expert_score = int(list_expert[len(list_expert)-1])
  # Set status high score menjadi False
  status = False
  # Jika modenya 'normal'
  if mode == 'normal':
    # Bagian Cetak Skor Normal
    # Jika high score
    if normal_score < score:
      status = True
      highscore.write(f"normal {pemain} {score}\n")
    # Jika tidak
    else:
      for kalimat in list_normal:
        if kalimat != list_normal[len(list_normal)-1]:
          print(kalimat, end=' ', file=highscore)
        else:
          print(kalimat, file=highscore)
    # Bagian Cetak Skor Expert
    for kalimat in list_expert:
      if kalimat != list_expert[len(list_expert)-1]:
        print(kalimat, end=' ', file=highscore)
      else:
        print(kalimat, file=highscore)
    print()
  # Jika modenya 'expert'
  else:
    # Bagian Cetak Skor Normal
    for kalimat in list_normal:
      # Jika belum sampai di bagian terakhir (bagian skor), jangan keluarkan newline
      if kalimat != list_normal[len(list_normal)-1]:
        print(kalimat, end=' ', file=highscore)
      else:
        print(kalimat, file=highscore)
    # Bagian Cetak Skor Expert
    # Jika high score
    if expert_score < score:
      status = True
      highscore.write(f"expert {pemain} {score}\n")
    # Jika tidak
    else:
      for kalimat in list_expert:
        # Jika belum sampai di bagian terakhir (bagian skor), jangan keluarkan newline
        if kalimat != list_expert[len(list_expert)-1]:
          print(kalimat, end=' ', file=highscore)
        else:
          print(kalimat, file=highscore)
  # Jangan lupa close file :D
  highscore.close()
  # Bagian Cetak
  if status:
    print("NEW HIGHSCORE!!!")
    print(f"Username : {pemain}")
    print(f"Score    : {score}")
    print(f"Berhasil meraih highscore mode {mode}.\n")
  print("~"*16 + " Thanks for playing " + "~"*16)

pemain, mode, score, nyawa, lagu = start_game()
score = game_on(score, nyawa)
highscore_part(pemain, mode, score)

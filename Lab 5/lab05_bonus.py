# Nama Program: Cari Soal
# Program ini dibuat oleh Muhammad Athallah (2020)
# hashtag #NoPlagiarisme ya, qaqa~

list_soal = [int(x) for x in input("Masukkan tingkat kesulitan soal: ​").split()]
soal_bocor = list_soal[0]
min = 0
indeks = 1
first = False
for kesulitan in range(1, len(list_soal)):
    if not first:
        first = True
        min = abs(soal_bocor - list_soal[kesulitan])
    if abs(soal_bocor - list_soal[kesulitan]) < min:
        min = abs(soal_bocor - list_soal[kesulitan])
        indeks = kesulitan
print(f"Versi soal paling mirip adalah soal ke: ​{indeks+1}")

#Program ini dibuat oleh Muhammad Athallah (2020)

#Inisiasi nilai koordinat
sumbuX = [0]
sumbuY = [0]

#Bagian input
print("### MEONG BROSSS (Speedrunning Mode) ###\n")
perintah = int(input("Masukkan banyak perintah yang ingin diberikan: "))
print()

#Mekanisme Program
for i in range(perintah):
    masukan = input("Masukkan perintah: ")
    if masukan == "HOME":
        break #perintah untuk exit mekanisme program
    elif masukan == "U":
        sumbuY[perintah+1]=sumbuY[perintah]+1 #bergerak ke utara
    elif masukan == "S":
        sumbuY[perintah+1]=sumbuY[perintah]-1 #bergerak ke selatan
    elif masukan == "T":
        sumbuX[perintah+1]=sumbuX[perintah]+1 #bergerak ke timur
    elif masukan == "B":
        ssumbuX[perintah+1]=sumbuX[perintah]-1 #bergerak ke barat

#Bagian Output
print("\nKarakter Meong Brosss berada di koordinat ({},{})\n".format(sumbuX,sumbuY))
print("### PROGRAM SELESAI ###")
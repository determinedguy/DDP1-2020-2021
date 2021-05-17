#Muhammad Athallah, 2020

#Bagian Input
print("***MY TACTICAL DOLL***")
my_name = input("Masukkan nama Tactical Doll: ")
my_power = int(input("Masukkan Firepower: "))
my_rate = int(input("Masukkan Rate of Fire: "))
my_accuracy = int(input("Masukkan Accuracy: "))
my_evasion = int(input("Masukkan Evasion: "))
print("")
print("***ENEMY TACTICAL DOLL***")
your_name = input("Masukkan nama Tactical Doll: ")
your_power = int(input("Masukkan Firepower: "))
your_rate = int(input("Masukkan Rate of Fire: "))
your_accuracy = int(input("Masukkan Accuracy: "))
your_evasion = int(input("Masukkan Evasion: "))

#Bagian Kalkulasi
my_dps = (my_power*my_rate)/60
my_effectiveness = 30*my_power+40*(my_rate**2)/120+15*(my_accuracy+my_evasion)
my_dps = round(my_dps,2)
my_effectiveness = round(my_effectiveness)
your_dps = (your_power*your_rate)/60
your_effectiveness = 30*your_power+40*(your_rate**2)/120+15*(your_accuracy+your_evasion)
your_dps = round(your_dps,2)
your_effectiveness = round(your_effectiveness)
if (my_dps >= your_dps and my_effectiveness >= your_effectiveness):
    hasil = "Lawan!"
else:
    hasil = "Lari!"

#Bagian Output
print("")
print("***CALCULATION**")
print(my_name)
print("Damage per Second:",my_dps)
print("Combat Effectiveness:",my_effectiveness)
print("")
print(your_name)
print("Damage per Second:",your_dps)
print("Combat Effectiveness:",your_effectiveness)
print("")

print("Kesimpulan:",hasil)
#Muhammad Athallah, 2020
print("***REQUEST TACTICAL DOLL***")

#Bagian Input
name = input("Masukkan nama Tactical Doll: ")
power = int(input("Masukkan Firepower: "))
rate = int(input("Masukkan Rate of Fire: "))
accuracy = int(input("Masukkan Accuracy: "))
evasion = int(input("Masukkan Evasion: "))

#Bagian Kalkulasi
dps = (power*rate)/60
effectiveness = 30*power+40*(rate**2)/120+15*(accuracy+evasion)
dps = round(dps,2)
effectiveness = round(effectiveness)

#Bagian Output
print("")
print("***SUCCESS***")
print("Tactical Doll:",name)
print("Firepower:",power)
print("Rate of Fire:",rate)
print("Accuracy:",accuracy)
print("Evasion:",evasion)
print("Damage per Second:",dps)
print("Combat Effectiveness:",effectiveness)
"""
Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

HH : Hours, 2 digits, range: 00 - 99

MM : Minutes, 2 digits, range: 00 - 59

SS : Seconds, 2 digits, range: 00 - 59

Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

def timeConverter(seconds):
      .....
 

Masukkan detik : 3600
Konversi : 01:00:00

Masukkan detik : 3665
Konversi : 01:01:05
Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

Masukkan detik : ujian
Invalid Input!

Masukkan detik : 20.5
Invalid Input!


Masukkan detik : -20
Invalid Input!
"""

# No 1 Elvin Fatkhunnuha

def timeConverter(input):
    HH = input//3600
    HH_modulus = input%3600
    MM = HH_modulus // 60
    MM_modulus = HH_modulus % 60
    SS = MM_modulus

    return "{:02d}:{:02d}:{:02d}".format(HH, MM, SS)



try:
    input= int(input("Masukkan input (detik): "))
    if input < 0 or input > 359999:
        print("Invalid input!")
    else:   
        print(timeConverter(input))
    

except: 
    print("Invalid input!")

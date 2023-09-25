print ("SELAMAT DATANG, SILAHKAN LOGIN TERLEBIH DAHULU")

user = "IPIT"
nim = "2309116016"
pw = "1919"


# Memeriksa username, NIM, dan password
def volume ()  :
    # BUAT INPUT UNTUK MEMASUKAN USERNAME, NIM DAN PASSWORD
    username_input = input("Masukkan Username: ")
    nim_input = input("Masukkan NIM: ")
    password_input= input("Masukkan Password: ")
    if username_input == user and nim_input == nim and password_input == pw:
        print(20*"=")
        print("ANDA BERHASIL LOGIN")
        print(20*"=")
   
        print("[1.]Bola")
        print("[2.]Tabung")
        print("[3.]Limas Segitiga")
        pilihan = int(input("Masukkan Pilihan [1/2/3/] :"))

#Menghitung voluume bola
        if pilihan == 1:
            r = float(input("Masukkan Jari-Jari: "))
            phi = 3.14
            hasil = 4/3 * phi * r * r * r
            print(f"VOLUME BOLA = {hasil}")
        elif pilihan == 2:
            r = float(input("Masukkan Jari-Jari: "))
            t = float(input("Masukkan tinggi: "))
            phi = 3.14
            hasil = phi * r * r * t
            print(f"VOLUME TABUNG = {hasil}")
        elif pilihan == 3:
            la = float(input("Masukkan luas alas: "))
            t = float(input("Masukkan tinggi: "))
            phi = 3.14
            hasil = 1/3 * la * t
            print(f"VOLUME LIMAS SEGITIGA = {hasil}")
    else : 
        print("SILAHKAN ULANG KEMBALI")
        volume()

volume ()

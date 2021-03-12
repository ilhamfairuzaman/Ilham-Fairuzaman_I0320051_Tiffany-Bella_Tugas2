# Penghitungan luas
def lpp():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas_pp = panjang * lebar
    print(luas_pp)

def ll():
    r = float(input("Masukkan jari jari lingkaran: "))
    luas_lingkaran = 3.14 * (r**2)
    print(luas_lingkaran)

def lk():
    sisi = float(input("Masukkan panjang rusuk kubus: "))
    luas_kubus = 6 * (sisi**2)
    print(luas_kubus)

def konversicf():
    celcius = float(input("Masukkan suhu dalam Celcius: "))
    fahrenheit = (9/5 * celcius) + 32
    print(fahrenheit)

def konversirk():
    reamur = float(input("Masukkan suhu dalam reamur: "))
    kelvin = (5/4 * reamur) + 273
    print(kelvin)

# Menampilkan menu
def show_menu():
    print ("============Perhitungan============")
    print ("1. Luas persegi panjang")
    print ("2. Luas lingkaran")
    print ("3. Luas kubus")
    print ("4. Konversi Celcius ke Fahrenheit")
    print ("5. Konversi Reamur ke Kelvin")
    print ("6. Exit")
    choice= input("Pilih perhitungan : ")

    # Menu lanjutan
    if choice == "1":
        lpp()
    elif choice == "2":
        ll()
    elif choice == "3":
        lk()
    elif choice == "4":
        konversicf()
    elif choice == "5":
        konversirk()
    elif choice == "6":
        exit()
    else:
        print("Input salah")

# Main Loop Program
if __name__ == "__main__": 
    while True :
        show_menu()



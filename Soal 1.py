# Menghitung luas persegi panjang
def luas_ppanjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    rumus_luas = panjang * lebar
    print("Luas persegi panjang =",rumus_luas)
    exit()

luas_ppanjang()

# Menghitung luas lingkaran
def luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    rumus_luas = 3.14 * jari_jari**2
    print("Luas lingkaran =",rumus_luas)
    exit()

luas_lingkaran()

# Menghitung luas kubus
def luas_kubus():
    sisi = float(input("Masukkan panjang rusuk kubus: "))
    rumus_luas = sisi **3
    print("Luas kubus",rumus_luas)
    exit()

luas_kubus()

# Program Konversi suhu celcius ke fahrenheit
def konversicf():
    celcius = float(input("Masukkan suhu dalam Celcius: "))
    rumus = (9/5 * celcius) + 32
    print(celcius, "derajat celcius sama dengan", rumus, "derajat fahrenheit")
    exit()

konversicf()

# Program Konversi suhu reamur ke kelvin
def konversirk():
    reamur = float(input("Masukkan suhu dalam reamur: "))
    rumus = (5/4 * reamur) + 273
    print(reamur, "derajat reamur sama dengan", rumus, "derajat kelvin")
    exit()

konversirk()




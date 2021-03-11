# Data
nama = "Ilham Fairuzaman"
panggilan = "Ilham"
sex = "laki-laki"
makanan_favorit = "Pisang goreng"
tinggi = 166
ukuran_sepatu = 40
ukuran_sepatu_cm = 26.5
pekerjaan = "Mahasiswa"
univ = "Universitas Sebelas Maret"
angkatan = 2020

# Menghitung umur
import datetime
waktu = datetime.datetime.now()

tahun_lahir = 2002
bulan_lahir = 2
tanggal_lahir = 8

umur_bulan = (waktu.year - tahun_lahir) * 12 + (waktu.month - bulan_lahir) + (waktu.day - tanggal_lahir)/30
umur_tahun = umur_bulan / 12
umur_hari = umur_bulan * 30

# Output
print("Profil singkat saya: ")
print(nama)
print(panggilan)
print(sex)
print(makanan_favorit)
print(tinggi, "cm")
print(pekerjaan)
print(univ)
print(angkatan)

# Menceritakan diri
print(
    "\nPerkenalkan, namaku", nama, "biasa dipanggil", panggilan,"umurku",
    round(umur_tahun, 2), "tahun", round(umur_bulan, 2), "bulan", round(umur_hari, 2), "hari. "
    "\nTinggiku", tinggi, "cm. ukuran sepatuku", ukuran_sepatu, "atau", ukuran_sepatu_cm, "cm. Makanan favoritku itu", makanan_favorit,
    "\nSekarang aku menjadi", pekerjaan, "di", univ, "dan aku angkatan", angkatan
    )
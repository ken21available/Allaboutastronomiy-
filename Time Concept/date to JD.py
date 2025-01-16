# Menghitung JD Dari Kalender Gregorian 
YY = int(input("masukan tahun :  "))
MM = int(input("masukan bulan (dalam angka) :  "))
DD = int(input("masukan hari atau tanggal :  "))


if MM <= 2 :
  YY = YY-1
  MM = MM + 12
  
A = int(YY/100)
B = 2 - A + int(A/4)

# julian day
JD = int(365.25 * (YY + 4716)) + int(30.6001 * (MM + 1)) + DD + B - 1524.5
print(f"jadi JD dari tanggal {DD} bulan {MM} Tahun {YY} adalah {JD}")


# Menghitung JD Dari Kalender julian 
YY = int(input("masukan tahun :  "))
MM = int(input("masukan bulan (dalam angka) :  "))
DD = int(input("masukan hari atau tanggal :  "))


if MM <= 2 :
  YY = YY-1
  MM = MM + 12
  
A = int(YY/100)
B = 0

# julian day
JD = int(365.25 * (YY + 4716)) + int(30.6001 * (MM + 1)) + DD + B - 1524.5
print(f"jadi JD dari tanggal {DD} bulan {MM} Tahun {YY} adalah {JD}")

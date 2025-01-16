# Konversi JD Ke Kalender Gregorian
JD =float(input("masukan nilai JD : "))

Z = int(JD + 0.5)
F = (JD +0.5) - Z

if Z < 2299161 :
  A = Z

if Z >= 2291161 :
  a = int((Z - 1867216.25) / 36524.25)
  A = Z + 1 + a - int( a / 4 )

B = A + 1524
C = int((B - 122.1) / 365.25)
D = int( 365.25 * C )
E = int( (B - D) / 30.6001)

# hitung tanggalnya
D = B - D - int(30.6001 * E) + F
DD = int(D)
DD1 = D - DD
jam = DD1 * 24
Jamreal = int(jam)
DD2 = jam - Jamreal
menit = DD2 * 60
menitreal = int(menit)
DD3 = menit - menitreal
detik = DD3 * 60
detikreal = int(detik)

if E < 14 :
  MM = E - 1       #jika E < 14
else :             #jika E = 14 atau 15
  MM = E - 13

if MM > 2 :
  YY = C - 4716    #jika MM > 2
else :             #jika MM = 1 atau 2
  YY = C - 4715

print(f"tahun {YY} , bulan {MM} , hari {DD}. jam {Jamreal}:{menitreal}:{detikreal}")


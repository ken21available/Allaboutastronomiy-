import math


def saha_logaritmik(T, G_r1, G_r, chi, Pe):
    # Konstanta dalam satuan SI
    k = 1.380649e-23       # J/K
    h = 6.62607015e-34     # Js
    m_e = 9.10938356e-31   # kg
    eV = 1.60218e-19       # J

    # konversi energi ionisasi ke Joule

    O = 5040/T
    # Saha equation (SI units)
    H1_Hn = (math.log10((2 * G_r1)/G_r)) + ((5/2)*math.log10(T)) - \
        (chi * O) - (math.log10(Pe)) - 0.48
    H1Hn = 10**H1_Hn

    return H1Hn


T = float(input("masukan nilai temperatur dalam kelvin = "))  # Kelvin
# Fungsi partisi ion H+ (proton)
G_r1 = float(input("masukan nilai bobot statistik n = "))
# Fungsi partisi atom H netral
G_r = float(input("masukan nilai bobot statistik 1 = "))
chi = float(input("masukan nilai Xion = "))  # eV
# dalam dyne/cm^2 kalau belum Pe = Pe_pascal * 10 agar ke dyne/cm^2
Pe = float(input("massukan nilai tekanan elektron = "))

Hasil = saha_logaritmik(T, G_r1, G_r, chi, Pe)
print(Hasil)


# R. Yudo arya Kusuma
# D4 Mi - A - 2020
# 20051397013

from this import s


class Persegi:
    def luas(s):
        hasil = s * s
        return hasil

    def keliling(s):
        hasil = s * 4
        return hasil


class Segitiga:
    def luas(a, t):
        hasil = a * t / 2
        return hasil

    def keliling(a, b, c):
        hasil = a + b + c
        return hasil


class JajarGenjang:
    def luas(a, t):
        hasil = a * t
        return hasil

    def keliling(a, b):
        hasil = 2 * (a + b)
        return hasil


print("Luas dan Keliling Persegi")
sisi = int(input("Masukkan sisi : "))
resLuas = Persegi.luas(sisi)
resKeliling = Persegi.keliling(sisi)
print("Luas persegi = " + str(resLuas))
print("Keliling persegi = " + str(resKeliling))
print("-------------------------------")
print("Luas Dan Keliling Segitiga")
a = int(input("Masukkan alas : "))
t = int(input("Masukkan Tinggi : "))
c = int(input("Masukkan Sisi Miring : "))
resLuasSegitiga = Segitiga.luas(a, t)
resKelilingSegitiga = Segitiga.keliling(a, t, c)
print("Luas Segitiga = " + str(resLuasSegitiga))
print("Keliling Segitiga = " + str(resKelilingSegitiga))
print("-------------------------------")
alas = int(input("Masukkan alas : "))
tinggi = int(input("Masukkan tinggi : "))
sisiMiring = int(input("Masukkan Sisi miring : "))
resLuasJajarG = JajarGenjang.luas(alas, tinggi)
resKelilingJajarG = JajarGenjang.keliling(alas, sisiMiring)
print("Luas Jajar Genjang = " + str(resLuasJajarG))
print("Luas Keliling Genjang = " + str(resKelilingJajarG))
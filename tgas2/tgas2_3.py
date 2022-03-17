class Balok:
    def volume(p, l, t):
        hasil = p * l * t
        return hasil


class Tabung:
    def volume(r, t):
        hasil = 3, 14 * r * r * t
        return hasil


class PrismaSegitiga:
    def volume(a, t, tPrisma):
        hasil = (a * t / 2) * tPrisma
        return hasil


print("Menghitung Volume Tabung")
r = float(input("Masukkan Jari-jari Tabung : "))
t = float(input("Masukkan Tinggi Tabung : "))
vTabung = Tabung.volume(r, t)
print("Volume Tabung = " + str(vTabung))
print("-------------------------------")
print("Menghitung Volume Balok")
p = int(input("Masukkan Panjang Balok : "))
l = int(input("Masukkan Lebar Balok : "))
tBalok = int(input("Masukkan Tinggi Balok : "))
vBalok = Balok.volume(p, l, tBalok)
print("Volume Balok = " + str(vBalok))
print("-------------------------------")
print("Menghitung Volume Prisma Segitiga")
a = float(input("Masukkan Alas Prisma : "))
tAlas = float(input("Masukkan Tinggi alas : "))
tPrisma = float(input("Masukkan Tinggi Prisma : "))
vPrisma = PrismaSegitiga.volume(a, tAlas, tPrisma)
print("Volume Prisma Segitiga = " + str(vPrisma))
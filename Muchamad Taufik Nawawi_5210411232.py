#Muchamad taufik nawawi
#5210411232
class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500)
minuman2 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000)
minuman3 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000)
minuman4 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500)

makanan1 = Menu("lesah", "soto dengan santan", 12000)
makanan2 = Menu("geprek nyos", "ayam geprek sambal matah", 25000)
makanan3 = Menu("orak arik", "telur campur sayuran", 8000)
makanan4 = Menu("magelangan", "nasigoreng mie", 10000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("taufik", "5210411232", "Informatika")
mahasiswa2 = Mahasiswa("Zidni", "5210411217", "Informatika")
mahasiswa3 = Mahasiswa("havin", "5210411212", "Informatika")
mahasiswa4 = Mahasiswa("ananda", "5210411247", "Informatika")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("arah langkah", "helman biopsa", 2003)
buku2 = Buku("arah suci", "calya putri", 2009)
buku3 = Buku("candaan malikat", "ranendra", 2007)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")


class Titik:
  def__init__(, x, y):
    self.x = x
    self.y = y

class Garis:
  def__init__(self, titik_pertama, titik_kedua):
    self.titik_pertama = titik_pertama
    self.titik_kedua = titik_kedua

  def panjang(self):
    pjg_x = self.titik_kedua.x - self.titik_pertama.x
    pjg_y = self.titik_kedua.y - self.titik_pertama.y
    pjg = (pjg_x*2 + pjg_y2) * 0.5
    return pjg

titik_a = Titik(0,0)
titik_b = Titik(3,4)
garis_ab = Garis(titik_a,titik_b)
print('pnjang garis ab adalah {}'.format(garis_ab.panjang()))
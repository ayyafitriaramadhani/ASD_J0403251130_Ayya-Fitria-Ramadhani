#=============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Latihan 5
# studi kasus generator PIN
#Generator PIN
#==============================================================

def buat_pin(panjang, hasil=""): 
 
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
 
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
 
buat_pin(8)

#penjelasan
'''
Fungsi ini menghasilkan seluruh kombinasi PIN dengan panjang tertentu menggunakan angka 0, 1, dan 2.
Jika panjang string hasil sudah sama dengan panjang PIN, kombinasi dicetak sebagai base case.
Jika belum, fungsi melakukan perulangan untuk setiap angka, menambahkan angka ke string saat ini, lalu memanggil dirinya sendiri secara rekursif.
Proses ini membentuk pohon rekursi dengan 3 cabang di setiap level, dan berulang sampai semua kombinasi PIN tercetak.
Setiap panggilan menunggu hasil panggilan berikutnya, kemudian kembali (backtracking) untuk mencoba cabang lain.
'''

#Bagaimana cara mencegah angka yang sama muncul berulang? 
'''Untuk mencegah angka yang sama muncul berulang dalam kombinasi atau PIN, 
kita perlu menambahkan pembatasan/pengecekan saat menambahkan angka baru.

caranya: 
1.Lihat angka terakhir yang sudah ada di string hasil. 
2.Saat memilih angka berikutnya, hanya tambahkan angka tersebut jika berbeda dari angka terakhir. 
3.Jika sama dengan angka terakhir, abaikan dan lanjut ke angka lain.
'''
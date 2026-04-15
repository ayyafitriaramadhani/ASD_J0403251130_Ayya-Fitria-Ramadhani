#=============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Latihan 4
# Backtracking dasar
#kombinasi huruf
#==============================================================

def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    kombinasi(n, hasil + "A") 
    kombinasi(n, hasil + "B") 
 
 
kombinasi(20)


#penjelasan
'''
fungsi dipanggil, dicek base case (panjang string = n), jika terpenuhi cetak hasil.
Jika belum, fungsi memanggil dirinya dua kali: menambahkan 'A' dan 'B' pada string saat ini.
Proses ini membentuk pohon rekursi dan berulang sampai semua kombinasi tercetak.
Setiap panggilan menunggu hasil panggilan berikutnya, lalu kembali (backtracking) untuk mencoba cabang lain.
'''


#bagaimana jumlah kombinasi yang dihasilkan. 
'''
Jumlah kombinasi yang dihasilkan oleh fungsi ini adalah 2^n, 
karena setiap karakter pada string bisa berupa 'A' atau 'B'. 
Misalnya, jika n = 20, maka total kombinasi yang tercetak adalah 2^20 atau 1.048.576 kombinasi.
'''
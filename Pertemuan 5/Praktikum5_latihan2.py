#=============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Latihan 2
#Tracking Rekursi
#==============================================================

def countdown(n): 
 
    if n == 0: 
        print("Selesai") 
        return 
    # Fase turun( sebelum rekursif memanggil)
    print("Masuk:", n) 
    #memanggil fungsi dengan n-1
    countdown(n - 1) 
    ## Fase naik / backtracking(setelah rekursif dipanggil)
    print("Keluar:", n) 
 
 
countdown(5)

#penjelasan
'''
 Fungsi berjalan secara rekursif dengan mencetak "Masuk: n"
 sampai mencapai base case (n == 0) yang mencetak "Selesai".
 Setelah itu, fungsi kembali (backtracking) dan mencetak
 "Keluar: n" dari angka terkecil ke terbesar, sehingga terlihat
 urutannya terbalik dibanding fase "Masuk".
'''

#Mengapa output 'Keluar' muncul terbalik? 
'''Perintah print("Keluar:", n) dieksekusi setelah pemanggilan rekursif 
selesai, sehingga terjadi saat fungsi kembali dari panggilan sebelumnya 
(fase backtracking). Karena rekursi bekerja seperti struktur tumpukan 
(stack) dengan prinsip LIFO, nilai yang terakhir masuk akan menjadi yang 
pertama keluar, sehingga urutan output “Keluar” muncul terbalik dibandingkan urutan “Masuk”.
'''

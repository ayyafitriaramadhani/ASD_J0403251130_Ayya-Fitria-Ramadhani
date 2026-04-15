#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#materi rekursif : konsep dasar backtracing
# Backtracking 1: Kombinasi Biner (n)
#==============================================================


def biner(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) 
        return 

    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
 
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 
 
biner(10)

#penjelasan
'''
untuk membangkitkan seluruh kemungkinan
 kombinasi bilangan biner sepanjang n digit.

 Setiap pemanggilan fungsi akan menambahkan
 dua kemungkinan angka, yaitu '0' dan '1',
 kemudian memanggil dirinya sendiri hingga
 panjang string mencapai n (base case).

 Ketika panjang string sudah sama dengan n,
 kombinasi tersebut dicetak sebagai output.

 Karena setiap digit memiliki 2 kemungkinan,
 maka total kombinasi yang dihasilkan adalah 2^n.
'''
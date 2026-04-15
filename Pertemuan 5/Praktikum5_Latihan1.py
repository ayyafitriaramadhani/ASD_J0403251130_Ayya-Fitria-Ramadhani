#=============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Latihan 1
# Rekursi pangkat
#==============================================================

def pangkat(a, n): 
    # Base case : jika pangkat n == 0, hasilnya 1
    if n == 0: 
        return 1 
    # Recursive case 
    return a * pangkat(a, n - 1) 
print(pangkat(4,3))

#penjelasan
'''Fungsi berjalan secara rekursif dengan mengalikan a
 satu per satu sampai mencapai base case (n == 0).
 Setelah base case tercapai, hasil dikembalikan dan
 dikalikan dari bawah ke atas sehingga diperoleh 4^3 = 64.
 '''
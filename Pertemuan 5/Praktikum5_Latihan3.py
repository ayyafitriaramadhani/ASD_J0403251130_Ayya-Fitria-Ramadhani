#=============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Latihan 3
# Rekursi pada list
#mencari nilai maksimum
#==============================================================

def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1: 
        return data[index] # kembalikan elemen terakhir sebagai maksimum sementara
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
    
    # Bandingkan elemen saat ini dengan maksimum sisa list
    if data[index] > maks_sisa: 
        return data[index]  # kembalikan elemen saat ini jika lebih besar
    else: 
        return maks_sisa  # kembalikan maksimum sisa list jika lebih besar
 
#list angka
angka = [-1 -10,-2,-4,0]
print("Nilai maksimum:", cari_maks(angka))

#penjelasan
'''
 1. Fungsi dipanggil pertama kali dengan index=0.
 2. Fungsi memeriksa base case:
   - Jika index sudah elemen terakhir, kembalikan elemen tersebut.
 3. Jika belum base case, lakukan recursive call:
   - panggil cari_maks(data, index+1) untuk mencari maksimum sisa list.
 4. Bandingkan elemen saat ini dengan hasil rekursi:
    - Jika elemen saat ini lebih besar, kembalikan elemen ini.
    - Jika tidak, kembalikan hasil maksimum dari sisa list.
 5. Proses ini berulang sampai seluruh elemen dibandingkan.
 6. Akhirnya, fungsi mengembalikan nilai maksimum dari seluruh list.
 '''
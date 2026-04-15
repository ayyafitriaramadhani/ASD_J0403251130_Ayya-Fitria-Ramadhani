#==============================
# Nama: Ayya Fitria Ramadhani
# NIM: J0403251130             
# Kelas: TPL B1                
#==============================

#===============================================
# Latihan 5: Melengkapi fungsi merge 
#===============================================
def merge(left, right):
    result = []
    i = 0
    j = 0 

    # Bandingkan elemen kiri dan kanan selama keduanya masih ada isi
    while i < len(left) and j < len(right):
#jawaban soal no 1 ()lengkapi kondisi agar menjadi asceding
        if left[i] <= right[j]:                 # Ambil nilai yang lebih kecil (ascending)
            result.append(left[i])              # Masukkan ke result
            i += 1                              # Geser pointer ke kiri
        else:
            result.append(right[j])             # Masukkan ke result 
            j += 1                              # Geser pointer ke kanan

    # Jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    # Jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

# ====================
# Panggil Program 
# ====================

left = [8, 14, 5]
right = [1, 7, 10, 45, 15]
hasil = merge(left, right)
print("Hasil Sorting: ", hasil)


#2. Jelaskan fungsi result.extend()!
'''
Jawaban:
fungsi tersebut berfungsi untuk menambahkan sisa elemen yang belum diproses 
ke dalam list result.
Hal ini dilakukan agar semua elemen tetap masuk ke hasil akhir setelah proses
perbandingan selesai.
'''
# ==========================================================
# Nama      :Ayya Fitria Ramadhani
# NIM       :J0403251130
# Kelas     :TPL-B1
# ==========================================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# masuk 1-2-3
# keluar
# ==========================================================

def hitung(n):
    # base case 
    if n == 0:
        print("Selesai.")
        return
    
    # Mencetak nilai sebelum pemanggilan rekursif 
    print("Masuk: ", n)
    
    # Recursive case: memanggil fungsi dengan n-1
    hitung(n-1) # recursive case
    
     # Mencetak nilai setelah rekursi selesai 
    print("Keluar.", n)

#program utama
print ("--- Program Tracing ---")
hitung (100)

#penjelasan
'''
1. Fungsi hitung(n) akan mencetak "Masuk: n" lalu memanggil dirinya
2. dengan nilai n-1 sampai n == 0.
3. Saat n == 0, program mencetak "Selesai." (base case).
4. Setelah itu fungsi kembali (backtracking) dan mencetak
5. "Keluar: n" dari angka terkecil sampai terbesar.
'''
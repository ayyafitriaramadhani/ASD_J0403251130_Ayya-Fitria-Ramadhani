#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#materi rekursif : faktorial
#recursive case => 3! = 3 x 2 x 1
#Base case => 0 berhenti
#==============================================================

def faktorial(n):
    #basecase
    # Jika n == 0, fungsi langsung mengembalikan 1
    if n == 0:
        return 1

    #recursive case
    # Jika n != 0, maka fungsi akan memanggil dirinya sendiri
    # dengan nilai (n-1)
    return n*faktorial(n-1)  #n-1*n-2*n-3..................n-?

#program utama dimulai dari sini
print("===== program faktorial =====")
print("hasil faktorial :", faktorial(3))

#penjelasan
'''
1. Program memanggil fungsi faktorial(3) 
2. Karena 3 != 0, maka dihitung 3 * faktorial(2) 
3. faktorial(2) → karena 2 != 0, dihitung 2 * faktorial(1) 
4. faktorial(1) → karena 1 != 0, dihitung 1 * faktorial(0) 
5. faktorial(0) → karena 0 == 0 (base case), mengembalikan 1 
6. Hasil kemudian dihitung kembali: 
    # faktorial(1) = 1 x 1 = 1
    # faktorial(2) = 2 x 1 = 2 
    # faktorial(3) = 3 x 2 = 6 
7. Program menampilkan hasil akhir: 6 
'''

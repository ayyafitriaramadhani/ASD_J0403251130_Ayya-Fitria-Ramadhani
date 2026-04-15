#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#materi rekursif : faktorial
#recursive case => 3! = 3 x 2 x 1
#Base case => 0 berhenti
#==============================================================

def jumlah_list(data, index=0):
    #base_case
    # Jika index sudah sama dengan panjang list,
    # berarti semua elemen sudah dijumlahkan
    if index == len(data):
        return 0
    
    #recursive case
    # Menjumlahkan elemen saat ini dengan hasil
    # pemanggilan fungsi untuk index berikutnya
    return data[index] + jumlah_list(data,index+1)

print("======program jumlah data list======")
print(jumlah_list([2,4,5]))

#Penjelasan
'''
1. Fungsi dipanggil dengan data = [2,4,5] dan index awal = 0.
2. Program akan menjumlahkan data[0] + data[1] + data[2]
3. secara rekursif sampai index sama dengan panjang list.
4. Saat index == 3 (panjang list), fungsi mengembalikan 0 (base case).
5. Kemudian hasil dijumlahkan dari belakang: (berurutan)
  5 + 0 = 5
  4 + 5 = 9
  2 + 9 = 11 (hasil penjumlahan sebelumnya di jumlahkan dengan sisa angka satu persatu)
6. Sehingga hasil akhirnya adalah 11.
'''
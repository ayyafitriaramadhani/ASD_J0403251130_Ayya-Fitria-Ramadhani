#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan 2 : Membuat fungsi load data
#===============================

nama_file = "data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file) :
    data_dict= {}# inisialisasi data dictionary

    with open ("data_mahasiswa.txt", "r", encoding="utf-8")as file:
        for baris in file:
            baris = baris.strip() #menghilangkan karakter baris baru
            parts= baris.split(",")
            if len (parts) != 3:
                continue 
            nim,nama,nilai_str = parts
            nilai_int= int(nilai_str)
            data_dict[nim]= {"nama " : nama ,"nilai " :nilai_int}
            nim, nama, nilai = baris.split(",")  # pisahkan data menadi satuan

        #simpan data mahasiswa di dictionary dengan key NIM
            data_dict[nim]= {         #key
                "nama": nama,         #value
                "nilai": int(nilai)   #value
            }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
buka_data= baca_data_mahasiswa(nama_file)
print("jumlah data terbaca", len(buka_data))

#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan  2 : Membuat fungsi menampilkan data
#===============================

def tampilkan_data(data_dict):

    if len (data_dict)== 0:
        print("Data Kosong")
        return
    
    #membuat header tabel
    print ("===== Daftar Mahasiswa =====")
    print(f"{'NIM' : <10} | {'Nama' :<12} | {'Nilai' :>5}")
    print("-"* 32)

    '''
    untuk tampilan yang rapi, atur f-string formating
        {'nim' : <10} artinya:
        tampilkan nim<= rata kiri dengan lebar 10 karakter
        {'nama' : <12} artinya: 
        tampilann nama rata kiri,dengan lebar kolom 12 karakter
        {'nilai' : <5} artinya: 
        tampilkan nilai rata kanan dengan  
    '''

    for nim in sorted(data_dict.keys()):
        nama= data_dict[nim]["nama"]
        nilai= data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama :<12} | {nilai:>5}")

#Memanggil fungsi menampilkan data
#tampilkan_data(buka_data)

#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan 2 : Membuat fungsi cari data
#===============================

def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan nim
    nim_cari= input("masukkan nim yang ingin di cari:").strip()

    if nim_cari  in data_dict:
        nama= data_dict[nim_cari]["nama"]
        nilai= data_dict[nim_cari]['nilai']
        
        print ("\n=== Data mahasiswa ditemukan===")
        print(f" NIM   : {nim_cari}")
        print(f" Nama  : {nama}")
        print(f" Nilai : {nilai}")

    else:
        print("\n Data Tidak ditemukan")
#cari_data(buka_data)


#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan 2 : Membuat fungsi update nilai
#===============================

def update_nilai(data_dict):
    #cari nim mahasiswa yang akan di update nilainya
    nim = input("Masukkan Nim mahasiswa yang akan diupdate  nilainya:").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukkan Nilai Baru (0-100):").strip())
    except ValueError:
        print("nilai baru berupa angka. update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru> 100:
        print("Nilai harus  antara o sampai 100. pembaharuan di batalkan!")

    nilai_lama= data_dict[nim]["nilai"]
    #memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"]= nilai_baru

    print(f"pembaruan berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}") 

#update_nilai(buka_data)


#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan 2 : Membuat fungsi menyimpan perubahan data ke file
#===============================

def simpan_data(nama_file, data_dict):
    with open (nama_file,"w", encoding ="utf-8")as file:
        for nim in sorted(data_dict.keys()):
            nama= data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("data berhasil disimpan")

#===============================
# Praktikum 2: Konsep ADT dan File Handling(studi kasus)
# Latihan 2 : Membuat menu program
#===============================

def main():
    #menalankan fungsi satu load data
    buka_data=baca_data_mahasiswa(nama_file)

while True:
    print("\n === MENU DATA MAHASISWA ====")
    print ("1. Tampilkan semua data") #fs 2
    print ("2. Cari data berdasarkan NIM") #fs 3
    print ("3. Update nnilai mahasiswa") #fs 4
    print ("4. simpan data ke file") #fs 5
    print ("0. keluar")

    pilihan = input("pilihan menu:").strip()

    if pilihan == "1":
        tampilkan_data(buka_data)
    elif pilihan == "2":
        cari_data (buka_data)
    elif pilihan == "3":
        update_data(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file,buka_data)
        print("Data Berhasil disimpan")

    elif pilihan == "0":
        print ("Program selesai")
        break

    else:
        print ("pilihan tidak valid.coba lagi!")

if __name__ == "__main__" :
    main()
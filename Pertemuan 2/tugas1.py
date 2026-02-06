# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Ayya Fitria Ramadhani
# NIM   : J0403251130
# Kelas : B1
# ========================================================== 
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
nama_file = "stok_barang.txt" 
# ------------------------------- 
# Fungsi: Membaca data dari file 
# -------------------------------

def baca_stok(nama_file):
   stok_dict = {} # inisialisasi data dictionary

   #Buka file dan baca seluruh baris
   with open ("stok_barang.txt", "r", encoding="utf-8")as file:
        for baris in file:
            baris = baris.strip() #menghilangkan \n
            parts= baris.split(",")
            if len (parts) != 3:
                continue 
            kodebarang,namabarang,stok_str = parts
            stok_int= int(stok_str)
            stok_dict[kodebarang]= {"Nama Barang " : namabarang ,"Stok " : stok_int}
            kodebarang, namabarang, stok = baris.split(",")  # pisahkan data menjadi satuan

        #simpan data stok barang di dictionary dengan key kode_barang
            stok_dict[kodebarang]= {          #key
                "Nama Barang": namabarang,    #value
                "Stok": int(stok)             #value
            }
        return stok_dict

#memanggil fungsi baca_stok
buka_data= baca_stok(nama_file)
print("jumlah data barang terbaca", len(buka_data))

# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 

def simpan_stok(nama_file, stok_dict): 

    #Menyimpan seluruh data stok ke file teks
    with open (nama_file,"w", encoding ="utf-8")as file:
        for kodebarang in sorted(stok_dict.keys()):
            namabarang= stok_dict[kodebarang]["Nama Barang"]
            stok = stok_dict[kodebarang]["Stok"]
            file.write(f"{kodebarang},{namabarang},{stok}\n")

simpan_stok(nama_file,buka_data)
print("data berhasil disimpan")

# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict):
    if len (stok_dict)== 0:
        print("Stok Kosong")
        return
    
    #membuat header tabel
    print (" ===== Daftar Barang =====")
    print(f"{"Kode Barang" : <12} | {"Nama Barang" :<15} | {'Stok' :>5}")
    print("-"* 40)

    for kodebarang in sorted(stok_dict.keys()):
        namabarang= stok_dict[kodebarang]["Nama Barang"]
        stok= stok_dict[kodebarang]["Stok"]
        print(f"{kodebarang: <12} | {namabarang :<15} | {stok:>5}")

#Memanggil fungsi menampilkan data
#tampilkan_semua(buka_data)

# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 

def cari_barang(stok_dict):

    #mencari data mahasiswa berdasarkan nim
    kode_cari= input("Masukkan Kode Barang: ").strip() #untuk menghilangkan \n

    if kode_cari  in stok_dict:
        namabarang= stok_dict[kode_cari]["Nama Barang"]
        stok= stok_dict[kode_cari]['Stok']
        
        print ("\n===Barang ditemukan===")
        print(f" Kode Barang   : {kode_cari}")
        print(f" Nama Barang   : {namabarang}")
        print(f" Stok          : {stok}")
        print()

    else:
        print("\n Barang tidak ditemukan")
        print()
#cari_barang(buka_data)

# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict):

    #menambahkan barang baru ke stok_dict
    kode= input("Masukkan kode barang baru: ").strip()     #menghilangkan \n

    #kode tidak boleh duplikat(validasi)
    if kode in stok_dict:
        print("kode sudah digunakan")
        return
    
    nama= input("Masukkan nama barang: ").strip()  #menghilangkan \n

    #input stok awal
    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0 :
            print("Stok tidak boleh kurang dari 0")
            return
    except ValueError:
        print("stok harus berupa angka!!")
        return
    
    #simpan ke dctionary
    stok_dict[kode]={
        "Nama Barang" : nama,
        "Stok"        : stok_awal
    }

    print("Barang baru berhasil di tambahkan")


# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 

def update_stok(stok_dict): 

    #cari nim mahasiswa yang akan di update nilainya
    kode_update = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    #Mengecek kode apakah ada di dalam stok_dict
    if kode_update not in stok_dict:
        print("Kode Barang tidak ditemukan")
        return
    
    #Menampilkan informasi barang
    print(f"Nama Barang   :  {stok_dict[kode_update]['Nama Barang']}")
    print(f"Stok saat ini :  {stok_dict[kode_update]['Stok']} \n")
    
    #Menampilkan pilihan jenis update
    print("=========Pilih jenis update=========")
    print("1. Tambah stok")
    print("2. Kurangi stok \n")

    #menginput pilihan user
    pilihan = input("Masukkan plihan (1/2): ").strip()

    #meminta jumlah perubahan stok
    try:
        jumlah= int(input("masukkan jumlah: "))
        if jumlah <= 0 :                  #validasi jumlah harus lebih dari 0
            print("Jumlah harus lebih dari 0.")
            return
    except ValueError:
        #jika jumlah input bukan angka.
        print(" Input Jumlah harus berupa angka!")
        return
    
    #Proses update stok
    if pilihan == "1":                #jika pilihan menambah stok
        stok_dict[kode_update]["Stok"]+= jumlah
        print(f"Stok berhasil ditambah.")
    elif pilihan == "2":              #jika pilihan mengurangi stok
        if stok_dict[kode_update]["Stok"] - jumlah < 0:             # mengecek agar stok tidak menjadi negatif
            print(f" Stok tidak boleh kurang dari 0. UPDATE DIBATALKAN!")
            return
        stok_dict[kode_update]["Stok"] -= jumlah
        print()
        print(f"Stok berhasil dikurangi!!")
    
    else :
        print ("Pilihan tidak valid")

    #menampilkan stok terbaru setelah update
    print(f"stok terbaru : {stok_dict[kode_update]["Stok"]}")

    update_stok(buka_data)

# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 

    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(nama_file) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input(" Pilih menu: ") 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(nama_file, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 

# Menjalankan program utama 
if __name__ == "__main__": 
    main() 

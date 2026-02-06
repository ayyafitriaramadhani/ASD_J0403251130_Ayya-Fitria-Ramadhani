#===============================
# Praktikum 1: Konsep ADT dan File Heading
# Latihan Dasar 1A : Membaca Seluruh Isi File
#===============================

#Membuka File dengan Mode Read ("r")
with open ("data_mahasiswa.txt","r", encoding ="utf-8") as file:
    isi_file= file.read() #membaca seluruh isi data 
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:",type(isi_file)) #Jenis tipe data
print("Jumlah Karakter ", len(isi_file)) #Meghitung Jumlah Karakter 
print("Jumlah Baris", isi_file.count("\n")+1) #Menghitung  Jumlah Baris


#Membuka File Perbaris
print("===Membaca File Perbaris===")
jumlah_baris = 0
with open ("data_mahasiswa.txt","r", encoding= "utf-8") as file:
    for baris in file:                 #Looping baris 
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()     #Menghilangkan Garis Baru \n (agar datanya murni dan tidak ada tambahan)
        print ("Baris ke -", jumlah_baris)
        print ("Isinya :", baris)


#===============================
# Praktikum 1: Konsep ADT dan File Heading
# Latihan Dasar 1B : Parsing baris menjadi kolom data
#===============================

with open ("data_mahasiswa.txt", "r", encoding="utf-8")as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai= baris.split(",")
        print ("NIM: ",nim ,"|Nama: ", nama ,"|Nilai: ", nilai)


#===============================
# Praktikum 1: Konsep ADT dan File Heading
# Latihan Dasar 1C : Membaca file dan menyimpan ke list
#===============================

data_list = [] # list untuk menampung data mahasiswa

with open ("data_mahasiswa.txt", "r", encoding="utf-8")as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")  # pisahkan data
        #Simpan Sebagai List "[nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalam LIST ===")
print (data_list)

print("=== Jumlah Record dalam LIST ===")
print ("Jumlah Record", len(data_list))

print("=== Menampilkan data record tertentu ===")
print ("Contoh record pertama: ", data_list[0])

#===============================
# Praktikum 1: Konsep ADT dan File Heading
# Latihan Dasar 1D : Membaca file dan menyimpan ke dictionary
#===============================

data_dict= {} # buat variable untuk dictionary
with open ("data_mahasiswa.txt", "r", encoding="utf-8")as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")  # pisahkan data

        #simpan data mahasiswa di dictionary dengan key NIM
        data_dict[nim]= {         #key
            "nama": nama,         #value
            "nilai": int(nilai)   #value
        }
    print ("===Data Mahasiswa dalam Dictionary===" )
    print(data_dict)
    
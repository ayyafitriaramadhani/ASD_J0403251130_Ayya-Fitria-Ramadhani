#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#srudi kasus: sistem antrian layanan akademik
#implementasi queue =>
# stack ==>front (masuk data dari depan) C-B-A-None
#enqueue (memindahkan pointer rear (menambah data baru dari belakang))
#dequeue (memindahkan poniter front (menghapus data dari depan))
#front ->  A-B-C yang di dequeue itu yang a (data yang duluan masuk)-> rear
#==============================================================

#1) mendefinisikan  node (unit dasar linked lisd) 
class node:
    def __init__(self,nim,nama):   #konstruktor
        self.nim  = nim #menyimpan NIM Mahasiswa
        self.nama = nama #menyimpan Naman Mahasiswa 
        self.next = None #pointer ke node berikutnya (namanya bisa next atau front)

#2) mendefinisikan queue, terdiri dari front dan rear. 
class queueakademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang(rear)
    def enqueue(self,nim,nama):
        nodebaru = node(nim,nama) #instantiasi
        #jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodebaru
            self.rear = nodebaru
            return
        
        #jika queue tidak kosong,maka data baru di letakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodebaru
        self.rear = nodebaru

    #menghapus data paling depan(memberikan layanan akademik)
    def dequeue(self):

        if self. is_empty():
            print("Antrian Kosong. Tidak  ada mahasiswa yang dilayani")
            return None
        
        #lihat data bagian front, simpan di variabel data yang akan dihapus(dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #Jika front menjadi none(data antrian  terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        print("\n Daftar antrian mahasiswa (front -> rear) :")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no},{current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program utama

def main():

    #instantiasi queue
    q = queueakademik()

    while True :
        print("====== Sistem Antrian Akademik ======")
        print("1. Tambah Mahasiwa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == "1":
            nim=input("Masukkan NIM : ").strip()
            nama= input("Masukkan Nama Mahasiswa : ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan ke Antrian")

        elif pilihan == "2":
           dilayani = q.dequeue()
           print(f"Mahasiswa dilayani :  {dilayani.nim}-{dilayani.nama}")
        
        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. Terima Kasih")
            break
        else:
            print("Pilihan tidak valid. silahkan coba lagi 1-4")

#penanda eksekusi file utama
if __name__ == "__main__":
    main()

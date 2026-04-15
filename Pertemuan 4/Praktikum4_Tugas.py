#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
# ========================================================== 

# ========================================================== 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
# ========================================================== 
 
# Membuat class node untuk menyimpan data pelanggan
class node: 
    def __init__(self, no, nama, servis): 
        self.no = no            #Nomor antrian
        self.nama = nama        #Nama pelanggan
        self.servis = servis    #Jenis servis
        self.next = None        # Pointer ke node berikutnya
 
 # Class QueueBengkel untuk mengatur sistem antrian
class QueueBengkel: 
    def __init__(self): 
        self.front = None 
        self.rear = None 
    
    def is_empty(self):
        return self.front is None
 
    #menambahkan data baru ke bagian belakang(rear)
    def enqueue(self, no, nama, servis): 
        nodebaru = node(no,nama,servis)   #instantiasi
       #jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
           self.front= nodebaru
           self.rear= nodebaru
           return
       
        #jika queue tidak kosong,maka data baru di letakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodebaru
        self.rear = nodebaru

     #menghapus data paling depan(memberikan layanan akademik)   
    def dequeue(self): 
        #jika antrian kosong
        if self.is_empty():
            print("Antrian Kosong. Tidak ada Pelanggan yang dilayani. ")
            return None
        
        #lihat data bagian front, simpan di variabel data yang akan dihapus(dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #Jika front menjadi none(data antrian  terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    #menampilkan seluruh isi antrian
    def tampilkan(self): 
        # Tampilkan seluruh antrian 
        print("\n Daftar antrian Pelanggan bengkel : ")
        #mulai dari front/head
        current = self.front
        no = 1
        
        #loop sampai data habis
        while current is not None:
            print(f"{no},{current.no},{current.nama},{current.servis}")
            current = current.next
            no += 1


#Program utama
def main(): 
    q = QueueBengkel()  #membuat objek antrian
 
    while True: 
        print("\n=== Sistem Antrian Bengkel ===") 
        print("1. Tambah Pelanggan") 
        print("2. Layani Pelanggan") 
        print("3. Lihat Antrian") 
        print("4. Keluar") 
 
        pilih = input("Pilih menu: ") 

        #menu tambah pelanggan
        if pilih == "1": 
            no = input("No Antrian : ") 
            nama = input("Nama      : ") 
            servis = input("Servis    : ") 
            q.enqueue(no, nama, servis) 
 
        #menu layani pelanggan
        elif pilih == "2": 
            q.dequeue() 
 
        #menu tampilkan antrian
        elif pilih == "3": 
            q.tampilkan() 

        #menu tampilkan antrian
        elif pilih == "4": 
            break 
 
        #keluar program
        else: 
            print("Pilihan tidak valid") 
 
 
if __name__ == "__main__": 
    main() 
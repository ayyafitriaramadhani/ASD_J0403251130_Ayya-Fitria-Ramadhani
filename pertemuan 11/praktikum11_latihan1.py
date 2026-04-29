#===================================
#Nama : ayya fitria ramadhani
#NIM  : J0403251130
#Kelas : TPL_B1

#Latihan 1 : BFS
#===================================

from collections import deque

# Representasi graph hubungan antar lokasi
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    # visited: untuk mencatat lokasi yang sudah dikunjungi agar tidak terjadi duplikasi
    visited = set()
    
    # queue: antrean untuk menyimpan lokasi yang akan diproses (Prinsip FIFO)
    queue = deque([start])
    
    # Tandai lokasi awal (Rumah) sebagai lokasi yang sudah dikunjungi
    visited.add(start)

    while queue:
        # Ambil lokasi dari antrean paling depan
        node = queue.popleft()
        
        # Tampilkan lokasi yang sedang dikunjungi
        print(node, end=" ")

        # Periksa semua lokasi tetangga (jalur yang terhubung langsung)
        for neighbor in graph[node]:
            # Jika lokasi tetangga belum pernah dikunjungi
            if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan ke dalam antrean untuk diproses pada tahap berikutnya
                queue.append(neighbor)

# Eksekusi program
print("BFS dari Rumah:")
bfs(graph, 'Rumah')

#pertanyaan analisis
'''
1. Node mana yang dikunjungi pertama?  
jawab: 'Rumah' karena start node
2. Mengapa BFS cocok untuk mencari jalur terdekat? 
jawab:  Karena BFS menelusuri secara melebar (level per level) atau bisa juga di sebut horizontal. Lokasi yang ditemukan lebih awal pasti memiliki jarak langkah yang lebih sedikit dari titik awal.
3. Apa perbedaan urutan BFS jika struktur graph diubah? 
jawab : kalau struktur berubah, urutan antrean (queue) otomatis berubah. Lokasi yang tadinya jauh bisa menjadi dekat kalau dihubungkan langsung ke node yang sedang diproses.
'''
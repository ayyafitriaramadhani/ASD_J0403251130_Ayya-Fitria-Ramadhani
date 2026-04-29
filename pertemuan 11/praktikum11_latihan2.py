#===================================
#Nama : ayya fitria ramadhani
#NIM  : J0403251130
#Kelas : TPL_B1

#Latihan 2 :DFS
#===================================

# Representasi graph untuk jalur eksplorasi
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    # Simpan semua node yang dikunjungi dalam list untuk pengaturan tanda koma
    path.append(node)

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dikunjungi, lakukan rekursif ke dalam
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Set untuk melacak node yang sudah dikunjungi
visited = set()
# List untuk menampung urutan agar bisa dicetak dengan koma
path = []

print("DFS dari A:")
dfs(graph, 'A', visited)

# Mencetak hasil dengan pemisah koma
print(", ".join(path))

#pertanyaan analisis
'''
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
jawaab: karena DSF cara kerjanya dengan menyelam (vertikal) yaitu mengeksekusi yang 1 dulu baru setelah selesai ke eksekusi berikutnya 
2. Apa yang terjadi jika urutan neighbor diubah?  
jawab : urutan kunjungan (output) akan berubah. Karena program memproses tetangga berdasarkan urutan di dalam list, jika urutan di list berubah, maka node yang dikunjungi lebih dulu pun akan berubah.
3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
Kalau pakai graph yang sama, hasil urutannya bakal beda karena cara jalannya nggak sama. DFS itu tipenya "menyelam", dia bakal telusuri satu jalur sampai mentok ke bawah (anak sampai cucunya) dulu, makanya urutannya jadi A, B, D, E, C, F. Sedangkan BFS itu lebih "melebar", dia bakal cek semua teman terdekatnya di satu level dulu sampai habis baru pindah ke level bawahnya, jadi urutannya lebih rapi yaitu A, B, C, D, E, F. Intinya, DFS itu fokus nyari yang paling dalam, kalau BFS fokus ngeratain semua yang terdekat dulu.
'''
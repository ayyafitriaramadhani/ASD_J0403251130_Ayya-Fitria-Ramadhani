#===================================
#Nama : ayya fitria ramadhani
#NIM : J0403251130
#Kelas : TPL_B1
#===================================

#===================================
#IMPLEMENTASI BFS
#===================================
#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph
graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F', 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]

}
def bfs(graph,start ):
    #fungsi untuk melakukan penelusuran graph dengan BFS
    #graph : dictionary yang menyimpan struktur dari graph
    #start : node aawal penelusuran

    #queue digunakanuntuk menyimpan node yang akan diproses/dibaca
    queue = deque()

    #variabel yang digunakan untuk menyimpan node yang sudah diproses/dibaca
    visited = set()

    #masukkan node awal ke queue
    queue.append(start)

    #tandai node awal sebagai node yang sudah di kunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()
        
        #Tampilkan node yang sedang di kunjungi
        print(node,end=" ")
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masuukan tetangga ke queue untuk di proses nanti
                queue.append(neighbor)

#menjalankan BFS dari node A 
bfs(graph, 'A')
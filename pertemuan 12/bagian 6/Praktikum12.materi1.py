#==================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path
#==================================

#==================================
#materi 2 = Algoritma Dijkstra
#==================================

import heapq # untuk menggunakan priority queue 
#membuat graph (bentuk dictionary) + setiap tetangga hrus memiliki bobot
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

#fungsi dijkstra
def dijkstra(graph, start):
    # Menyimpan jarak minimum dari node awal ke semua kode (aawalnya semua jarak di isi tak hingga(inf))
    distances = {node: float('inf') for node in graph}
    
    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0
    
    # Priority queue
    pq = [(0, start)]
    
    while pq:
        #mengambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            
            #menghitung jarak baru ke tetangga
            distance = current_distance + weight
            
            # Jika ditemukan jarak lebih kecil dari sebelumnya
            if distance < distances[neighbor]:
                
                #update jarak yg lebih kecil
                distances[neighbor] = distance
                
                #masuk ke dalam antrian
                heapq.heappush(pq, (distance, neighbor))
    #mengembalikan hasil jarak minimum
    return distances

#menjalankan fungsi dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')
#menampilkan hasil jarak terpendek
print(hasil)
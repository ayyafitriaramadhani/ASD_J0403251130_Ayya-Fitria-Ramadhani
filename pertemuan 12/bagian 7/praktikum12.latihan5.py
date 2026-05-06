#=====================================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path
#=====================================================

#=====================================================
# Praktikum: Dijkstra - Jalur Terpendek Antar Kota
#=====================================================

import heapq  # untuk priority queue

# 1. Representasi graph berbobot (jarak antar kota)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Menyimpan jarak terpendek (awal = tak hingga)
    distances = {node: float('inf') for node in graph}
    
    # Jarak ke node awal = 0
    distances[start] = 0
    
    # Priority queue (jarak, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika jarak lebih besar, lewati
        if current_distance > distances[current_node]:
            continue
        
        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


# 3. Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# 4. Output hasil
print("Jarak terpendek dari Bogor:")
for node, distance in hasil.items():
    print("Bogor ->", node, "=", distance)

# pertanyaan Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

#jawaban analisis :
# 1. Node awal yang digunakan adalah Bogor
# 2. Node dengan jarak paling kecil dari Bogor adalah Depok dengan jarak 2
# 3. Node dengan jarak paling besar dari Bogor adalah Bandung dengan jarak 8
# 4. Cara kerja Dijkstra pada kasus ini:
    # - Mulai dari Bogor (jarak = 0)
    # - Cek semua tetangga (Jakarta = 5, Depok = 2)
    # - Pilih jarak paling kecil dulu (Depok)
    # - Dari Depok:
        #   Depok -> Jakarta = 2 + 2 = 4 (lebih kecil dari 5, jadi diupdate)
        #   Depok -> Bandung = 2 + 6 = 8
    # - Lanjut ke node dengan jarak kecil berikutnya (Jakarta = 4)
    # - Dari Jakarta ke Bandung = 4 + 7 = 11 (lebih besar dari 8, jadi diabaikan)
    # - Hasil akhir didapat jarak terpendek ke semua kota
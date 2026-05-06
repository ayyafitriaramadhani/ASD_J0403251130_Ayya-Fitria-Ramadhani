#=====================================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path
#=====================================================

#=====================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
#=====================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Semua jarak awal tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start = 0
    distances[start] = 0
    
    # Priority queue
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak lebih besar, skip
        if current_distance > distances[current_node]:
            continue
        
        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# pertanyaan Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?


#jawaban analisis
# 1. Lokasi paling dekat dari Gerbang adalah Kantin
    # karena jaraknya paling kecil yaitu 2 menit
# 2. Waktu tempuh terpendek dari Gerbang ke Aula = 7 menit
    # jalurnya: Gerbang -> Kantin -> Lab -> Aula
    # = 2 + 4 + 1 = 7
# 3. Jalur langsung tidak selalu paling kecil
# contoh:
    # Gerbang -> Aula langsung lewat Kantin = 2 + 7 = 9
    # tapi lewat Lab: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 (lebih kecil)
# 4. Dijkstra cocok karena semua bobot bernilai positif (waktu tempuh) dan algoritma ini efisien untuk mencari jalur terpendek dalam graph seperti peta lokasi kampus
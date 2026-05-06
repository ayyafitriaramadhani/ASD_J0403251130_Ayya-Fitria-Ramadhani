#==================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path
#==================================

#==================================
#materi 2 = Algoritma Bellman Ford
#==================================


#graph berbentuk dictionary
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

#fungsi algoritma Bellman-Ford
def bellman_ford(graph, start):
    #membuat dictionary untuk menyimpan jarak dari node awal (awalnya semua jarak = tak hingga(inf))
    distances = {node: float('inf') for node in graph}
    #jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Relaksasi berulang (untuk mencari jarak terpendek)
    for _ in range(len(graph) - 1):
       
       #loop setiap node 
        for node in graph:
 
            #loop setiap tetangga dan bobotnya
            for neighbor, weight in graph[node].items():
                
                if distances[node] + weight < distances[neighbor]:
                    
                    #update jarak ke tetangga
                    distances[neighbor] = distances[node] + weight
    
    #mengembalikan hasil jarak terpendek
    return distances

# Menjalankan algoritma dari node 'A'
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil jarak terpendek
print(hasil)

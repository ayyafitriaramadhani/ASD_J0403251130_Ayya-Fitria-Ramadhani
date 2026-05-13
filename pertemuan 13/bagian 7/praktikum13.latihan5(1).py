# ===============================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree 
# ===============================================

# ===============================================
# Latihan 5 : Buat Program MST dengan Kasus Baru 
# Kasus 1 . Jaringan Jalan Antar Kota 
# ===============================================

import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge sementara
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            # Menambahkan node ke visited
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot
            total_weight += weight

            # Memasukkan edge baru
            for neighbor, w in graph[v].items():

                # Hanya node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST
    return mst, total_weight


# Menjalankan algoritma Prim dari Bogor
mst, total = prim(graph, 'Bogor')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total)


# Pertanyaan dan Jawaban Analisis

# 1. Kasus apa yang dipilih?
'''Kasus yang dipilih adalah kasus 1. Jaringan Jalan Antar Kota.'''

# 2. Algoritma apa yang digunakan?
''' Algoritma yang digunakan adalah Prim.'''

# 3. Edge mana saja yang dipilih dalam MST?
'''Edge yang dipilih:
Bogor - Depok = 2
Depok - Jakarta = 3
Depok - Bandung = 4'''

# 4. Berapa total bobot MST?
'''Total bobot MST adalah 9.'''

# 5. Mengapa edge tertentu tidak dipilih?
'''Karena edge tersebut memiliki bobot lebih besar atau dapat membentuk cycle.'''
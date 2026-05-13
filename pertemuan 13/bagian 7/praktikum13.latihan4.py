# ====================================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree 
# ====================================================

# ====================================================
# Latihan 4:  Studi Kasus: Jaringan Kabel Antar Gedung
# ====================================================

import heapq

# Representasi weighted graph
# Format:
# 'Node': {'Tetangga': bobot}
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan gedung yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge yang akan dipilih
    edges = []

    # Memasukkan edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total biaya
    total_cost = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika gedung tujuan belum dikunjungi
        if v not in visited:

            # Menandai gedung sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan biaya
            total_cost += weight

            # Memasukkan edge baru dari node tersebut
            for neighbor, w in graph[v].items():

                # Hanya node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total biaya
    return mst, total_cost


# Menjalankan algoritma Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")

for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)


# Pertanyaan dan Jawaban Analisis:

# 1. Algoritma apa yang digunakan?
'''Program menggunakan algoritma Prim.'''

# 2. Edge mana saja yang dipilih?
'''Edge yang dipilih adalah:
GedungA - GedungC = 2
GedungC - GedungD = 1
GedungD - GedungB = 3'''

# 3. Berapa total biaya minimum?
'''Total biaya minimum adalah 6.'''

# 4. Mengapa MST cocok digunakan pada kasus ini?
'''Karena MST dapat menghubungkan semua gedung
dengan biaya paling minimum tanpa jalur berulang.'''
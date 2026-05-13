# ====================================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree 
# ====================================================

# ====================================================
# Latihan 3: Implementasi algoritma prim
# ====================================================

import heapq

# Graph dalam bentuk dictionary
# Setiap node memiliki tetangga dan bobot edge
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge yang akan dipilih
    edges = []

    # Memasukkan edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot MST
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total
            total_weight += weight

            # Menambahkan edge baru dari node tersebut
            for neighbor, w in graph[v].items():

                # Hanya node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)


# Pertanyaan dan Jawaban Analisis:

# 1. Node awal apa yang digunakan?
'''Node awal yang digunakan adalah node A.'''

# 2. Edge mana yang dipilih pertama kali?
'''Edge ('A', 'C') dengan bobot 2 dipilih pertama kali
karena memiliki bobot paling kecil dari node A.'''

# 3. Bagaimana Prim menentukan edge berikutnya?
'''Prim memilih edge dengan bobot paling kecil
yang menghubungkan node yang sudah dikunjungi
ke node yang belum dikunjungi.'''

# 4. Berapa total bobot MST yang dihasilkan?
'''Total bobot MST yang dihasilkan adalah 6.'''

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
'''Prim memulai dari satu node lalu memperluas tree,
sedangkan Kruskal memilih edge terkecil dari seluruh graph.'''
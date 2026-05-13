# ==========================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================

# ==========================================
# Materi 2: Implementasi Algoritma Prim
# ==========================================

# Mengimpor library heapq
# untuk mengambil bobot terkecil
import heapq

# Representasi weighted graph
# Format:
# 'Node': {'Tetangga': bobot}
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

    # Menyimpan edge sementara
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

            # Mengecek tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika node belum dikunjungi
                if neighbor not in visited:

                    # Memasukkan edge baru ke heap
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)

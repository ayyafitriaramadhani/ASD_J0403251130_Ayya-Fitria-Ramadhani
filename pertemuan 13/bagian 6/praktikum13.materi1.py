# ==========================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================

# ==========================================
# Materi 1: Implementasi Algoritma Kruskal
# ==========================================

# Daftar edge dalam bentuk: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge dari bobot terkecil ke bobot terbesar
edges.sort()

# List untuk menyimpan hasil MST
mst = []

# Variabel untuk menyimpan total bobot
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk mengecek setiap edge
for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)
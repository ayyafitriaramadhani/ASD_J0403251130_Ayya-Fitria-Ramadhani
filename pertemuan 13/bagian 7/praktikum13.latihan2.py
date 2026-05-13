# ====================================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree 
# ====================================================

# ====================================================
# Latihan 2: Implementasi sederhana algoritma kruskal
# ====================================================

# Daftar edge dalam bentuk: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge dari bobot terkecil ke terbesar
edges.sort()

# Menyimpan edge yang masuk ke MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk memilih edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
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

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)


# Pertanyaan dan Jawaban Analisis:

# 1. Edge mana yang dipilih pertama kali?
'''Edge ('C', 'D') dengan bobot 1 dipilih pertama kali
karena memiliki bobot paling kecil.'''

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
'''Karena tujuan MST adalah mendapatkan total bobot
paling minimum, jadi edge terkecil diprioritaskan.'''

# 3. Berapa total bobot MST yang dihasilkan?
'''Total bobot MST yang dihasilkan adalah 6.'''

# 4. Mengapa edge tertentu tidak dipilih?
'''Karena edge tersebut dapat membentuk cycle
atau sudah ada jalur yang menghubungkan node tersebut.'''
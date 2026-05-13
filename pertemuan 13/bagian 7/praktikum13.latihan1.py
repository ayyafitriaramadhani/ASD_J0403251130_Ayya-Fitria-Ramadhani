# ==========================================
# Nama : Ayya Fitria Ramadhani
# NIM : J0403251130
# Kelas : TPL_B1
# Praktikum 13 - Graph III: Spanning Tree 
# ==========================================

# ==========================================
# Latihan 1: Memahami konsep spanning tree
# ==========================================

# Daftar edge pada graph
# Edge adalah hubungan antar titik (vertex)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
# Spanning tree menghubungkan semua titik tanpa ada jalur yang berputar (cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan semua edge pada graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Memberi jarak antar output
print("\nSpanning Tree:")

# Menampilkan edge pada spanning tree
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge pada graph awal
print("\nJumlah edge graph =", len(edges))

# Menampilkan jumlah edge pada spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))


# Pertanyaan dan Jawaban Analisis:

# 1. Apa perbedaan graph awal dan spanning tree?
'''Graph awal memiliki semua hubungan antar titik,
sedangkan spanning tree hanya mengambil beberapa edge
untuk menghubungkan semua titik tanpa cycle.'''

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
'''Karena jika ada cycle, maka jalurnya menjadi berputar
dan tidak termasuk tree yang sederhana.'''

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
'''Karena spanning tree hanya mengambil edge yang diperlukan
untuk menghubungkan semua titik tanpa jalur tambahan.'''
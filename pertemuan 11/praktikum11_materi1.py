#===================================
#Nama : ayya fitria ramadhani
#NIM : J0403251130
#Kelas : TPL_B1
#===================================

#===================================
#IMPLEMENTASI DASAR GRAPH
#===================================
graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C']

}
for node in graph:
    print(node,"->", graph[node])
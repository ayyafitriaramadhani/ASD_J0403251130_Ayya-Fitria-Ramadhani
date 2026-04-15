def fact_rec(n):
    #kondisi terminal
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    #pemanggilan rekrusif(fase awal)
    else:
        return n* fact_rec(n-1)
    
print ("Hasil rekrusif 4! adalah ",fact_rec(4))
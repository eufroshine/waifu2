# input nilai intenger
n = int(input("Masukan nilai n: "))
t = int(input("Masukan nilai t: "))

# cetak nilai variabel
print("Variabel n:", n)
print("Variabel t:", t)

# cetak hasil operasi kedua variabel dengan format string
print("Hasil penggabungan {0} & {1}: %d".format(n, t) % (n + t))

# konversi nilai variabel
n = int(n)
t = int(t)
print("Hasil penjumlahan {0} + {1}: %d".format(n, t) % (n + t))
print("Hasil pembagian {0} / {1}: %d".format(n, t) % (n / t))

## Mata Kuliah

Sebagai tugas praktikum: [2] Bahasa Pemrograman | Universitas Pelita Bangsa.

## Laporan Praktikum

- Latihan 1:

  > Python bersifat case-sensitive, jadi perhatikan besar kecil huruf yang digunakan.

  <p align="left">
    <img src="/ss/1.jpg" width="500">
  </p>

      # print digunakan untuk mencetak suatu perintah
      print("Hello!")
      print("6xatz: sedang belajar Python.")

perintah **\*print** ini berfungsi untuk mencetak suatu kata maupun perintah pada Python.

- Latihan 2:

  > **_a + b_** bisa saja ditulis menjadi **_a+b_** tapi penggunaan Python mempunyai standar keteraturan.

  <p align="left">
    <img src="/ss/2.jpg" width="330">
  </p>

      # variabel
      a = 69
      b = 666

      # cetak dan hitung variabel
      print("Nilai pertama:", a)
      print("Nilai kedua:", b)
      print("Hasil dari kedua nilai:", a + b)

**_a = 69_** dan **_b = 666_** merupakan sebuah variabel dan intenger.
**_, a + b_** merupakan perintah pada Python untuk menjumlahkan variabel yang tertera.

- Latihan 3:

  > **_int_** bersifat opsional, gunakan jika ingin kode lebih terstruktur.

  <p align="left">
    <img src="/ss/3.jpg" width="400">
  </p>

      # input nilai variabel bersifat intenger
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

**_int_** berfungsi untuk mendefinisikan sifat perintah menjadi bilangan bulat.
**_input_** berfungsi untuk memasukan kata atau bilangan yang diinginkan.
**_, n_** dan **_, t_** berfungsi untuk meletakan variabel yang sudah didefinisikan sebelumnya.
**_{0}_** dan **_{1}_** berfungsi untuk memanggil variabel sesuai urutan.
**_%d_** merupakan hasil dengan definisi sesuai pada **_.format_**.

## Documentation

All associated resources. are licensed under the [MIT License](https://mit-license.org/).

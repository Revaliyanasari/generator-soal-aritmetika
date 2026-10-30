# Pengujian Generator Soal Aritmetika

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan bahwa program Generator Soal Aritmetika dapat menghasilkan soal secara acak, memeriksa jawaban pengguna, menghitung nilai akhir, serta menangani input yang tidak valid.

## 2. Daftar Test Case

| ID | Fitur yang Diuji | Input atau Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Penjumlahan | Memilih operasi 1 | Program menampilkan soal penjumlahan |
| TC02 | Pengurangan | Memilih operasi 2 | Program menampilkan soal pengurangan |
| TC03 | Perkalian | Memilih operasi 3 | Program menampilkan soal perkalian |
| TC04 | Pembagian | Memilih operasi 4 | Program menampilkan soal pembagian dengan hasil bilangan bulat |
| TC05 | Pemeriksaan jawaban benar | Jawaban pengguna sama dengan jawaban yang benar | Program menampilkan pesan "Benar!" |
| TC06 | Pemeriksaan jawaban salah | Jawaban pengguna berbeda dari jawaban yang benar | Program menampilkan jawaban yang benar |
| TC07 | Validasi jumlah soal | Memasukkan angka 0 | Program menolak jumlah soal |
| TC08 | Validasi pilihan operasi | Memasukkan pilihan 9 | Program menampilkan pesan "Pilihan tidak valid." |
| TC09 | Validasi input jawaban | Memasukkan teks `abc` | Program menampilkan pesan kesalahan dan meminta jawaban kembali |
| TC10 | Perhitungan nilai | 4 jawaban benar dari 5 soal | Fungsi perhitungan menghasilkan nilai 80 |

## 3. Hasil Pengujian Aktual

| ID | Hasil Aktual | Status |
|---|---|---|
| TC01 | Program berhasil menampilkan soal penjumlahan secara acak | Berhasil |
| TC02 | Program berhasil menampilkan soal pengurangan secara acak | Berhasil |
| TC03 | Program berhasil menampilkan soal perkalian secara acak | Berhasil |
| TC04 | Program berhasil menampilkan soal pembagian dengan hasil bilangan bulat | Berhasil |
| TC05 | Program menampilkan pesan "Benar!" ketika jawaban pengguna benar | Berhasil |
| TC06 | Program menampilkan jawaban yang benar ketika jawaban pengguna salah | Berhasil |
| TC07 | Program menolak jumlah soal 0 dan menampilkan pesan yang sesuai | Berhasil |
| TC08 | Program menampilkan pesan "Pilihan tidak valid." ketika pengguna memasukkan pilihan 9 | Berhasil |
| TC09 | Program menampilkan pesan kesalahan dan meminta jawaban kembali ketika pengguna memasukkan teks `abc` | Berhasil |
| TC10 | Fungsi perhitungan menghasilkan nilai 80 untuk 4 jawaban benar dari 5 soal | Berhasil |

## 4. Kesimpulan Pengujian

Berdasarkan pengujian yang telah dilakukan, seluruh 10 test case berhasil dijalankan sesuai dengan hasil yang diharapkan. Program dapat menghasilkan soal aritmetika, memeriksa jawaban, menghitung nilai akhir, dan menangani beberapa kondisi input yang tidak valid.

Pengujian dilakukan melalui terminal Visual Studio Code. Dokumentasi ini digunakan untuk mencatat skenario pengujian dan hasil yang diperoleh selama pengujian program.
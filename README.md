# Generator Soal Aritmetika

## Deskripsi

Generator Soal Aritmetika merupakan program berbasis Python yang dirancang untuk menghasilkan soal aritmetika secara otomatis. Program ini dikembangkan untuk membantu pengguna memperoleh latihan soal matematika secara praktis.

Melalui program ini, proses pembuatan soal aritmetika dapat dilakukan menggunakan komputer tanpa harus menyusun setiap soal secara manual. Program ini diharapkan dapat membantu pengguna berlatih dan meningkatkan pemahaman terhadap operasi aritmetika.

Pengguna sasaran program ini adalah siswa, mahasiswa, pendidik, serta pengguna lain yang membutuhkan latihan soal aritmetika.

## Fitur

- Menghasilkan soal aritmetika melalui program Python.
- Memproses pembuatan soal berdasarkan logika program yang telah diimplementasikan.
- Menampilkan soal yang dihasilkan melalui terminal.
- Memisahkan bagian program ke dalam beberapa modul agar kode lebih terstruktur dan mudah dipelihara.

## Persyaratan

- Python 3.x
- Visual Studio Code sebagai editor kode yang disarankan.

## Cara Menjalankan

1. Buka folder proyek `generator-soal-aritmetika` menggunakan Visual Studio Code.
2. Buka terminal melalui menu **Terminal → New Terminal**.
3. Pastikan terminal berada di direktori utama proyek yang berisi file `main.py`.
4. Jalankan program menggunakan perintah berikut:

   ```bash
   python main.py
   ```

   Jika perintah tersebut tidak berfungsi pada Windows, gunakan:

   ```bash
   py main.py
   ```

5. Ikuti instruksi yang ditampilkan oleh program, jika tersedia.
6. Periksa soal aritmetika yang dihasilkan melalui terminal.

## Struktur Folder

```text
generator-soal-aritmetika/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/
```

Keterangan:

- `README.md`: dokumentasi proyek yang menjelaskan deskripsi, fitur, cara menjalankan program, dan hasil pengujian.
- `.gitignore`: menentukan file atau folder yang tidak perlu disertakan dalam repositori Git.
- `main.py`: file utama untuk menjalankan program dan mengatur alur eksekusi.
- `src/`: folder yang berisi modul-modul Python.
- `src/__init__.py`: file penanda paket Python pada folder `src`.
- `src/input_data.py`: modul untuk menangani input pengguna apabila diperlukan.
- `src/proses.py`: modul yang menangani logika utama pembuatan soal aritmetika.
- `src/output.py`: modul untuk menampilkan hasil program.
- `data/contoh_data.txt`: file untuk menyimpan data contoh apabila diperlukan oleh program.
- `tests/test_case.md`: dokumentasi skenario dan hasil pengujian program.
- `docs/screenshot/`: folder untuk menyimpan tangkapan layar implementasi dan pengujian program.

## Test Case

Pengujian dilakukan untuk memastikan program dapat dijalankan dan fungsi-fungsi yang telah diimplementasikan bekerja sesuai dengan hasil yang diharapkan.

Berdasarkan uji coba yang telah dilakukan, seluruh skenario pengujian yang dicantumkan dinyatakan berhasil.

| ID | Skenario Pengujian | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC01 | Menjalankan program | Program berjalan tanpa kesalahan | Program berjalan sesuai harapan | PASS |
| TC02 | Menghasilkan soal aritmetika | Soal berhasil dihasilkan | Soal berhasil dihasilkan | PASS |
| TC03 | Memeriksa tampilan soal | Soal ditampilkan melalui terminal | Soal ditampilkan sesuai harapan | PASS |
| TC04 | Memeriksa proses aritmetika, apabila terdapat perhitungan jawaban | Hasil perhitungan sesuai dengan operasi yang digunakan | Proses berjalan sesuai harapan | PASS |
| TC05 | Memeriksa input tidak valid, apabila program menerima input | Program menangani input sesuai rancangan | Program berjalan sesuai harapan | PASS |

**Kesimpulan pengujian:** Seluruh skenario yang diuji berhasil dijalankan sesuai dengan hasil yang diharapkan.

## Known Issues

- Pengembangan fitur dapat disesuaikan dengan kebutuhan pengguna dan tujuan pembelajaran.
- Variasi jenis soal dan tingkat kesulitan dapat dikembangkan lebih lanjut apabila belum tersedia dalam versi program saat ini.

## Anggota dan Kontribusi

- **Nama anggota:** [Isi dengan nama lengkap]
- **Kontribusi:** Melakukan implementasi program Generator Soal Aritmetika menggunakan Python, menjalankan pengujian program, serta menyusun dokumentasi proyek.

## Referensi/Bantuan

1. Bahan Ajar Algoritma dan Pemrograman Pertemuan 15: *Implementasi, Pengujian, dan Dokumentasi Proyek Python di VS Code, Git, dan GitHub*.
2. Python Software Foundation. Dokumentasi resmi Python: https://docs.python.org/3/
3. Microsoft. Dokumentasi Visual Studio Code: https://code.visualstudio.com/docs
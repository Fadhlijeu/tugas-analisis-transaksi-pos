# Analisis Transaksi POS 2024–2025

Repository ini berisi dua notebook pengolahan data transaksi POS dengan dataset yang sama.

Dataset: `paket_a_transaksi_pos_2024_2025.csv`.

## Daftar Tugas

### Tugas 1 — Analisis Pendapatan

File: `analisis_transaksi_pos.ipynb`

- Memeriksa duplikat dan nilai kosong.
- Membersihkan format tanggal dan harga.
- Memeriksa kuantitas yang tidak wajar.
- Menghitung pendapatan bersih tahun 2024 dan 2025.
- Menyimpan ringkasan pendapatan dan grafik.

### Tugas 2 — Manipulasi Data dengan Pandas

File: `tugas_manipulasi_data_pandas.ipynb`

- Membersihkan format harga dan mengubah tipe data menjadi numerik.
- Mengubah kuantitas negatif menjadi positif.
- Mengisi kode kasir kosong dan memilih kolom dengan `.iloc[]`.
- Menghitung omzet kotor, diskon, omzet bersih, dan PPN 11%.
- Menyaring dan mengurutkan transaksi.
- Membuat laporan gerai dengan `.groupby()`, `.agg()`, dan `.transform()`.

Kedua tugas berada dalam file notebook yang berbeda. Tugas 2 membaca dataset langsung dari CSV asli.

## Hasil Analisis Pendapatan

| Tahun | Jumlah Transaksi | Total Barang | Pendapatan Kotor | Total Diskon | Pendapatan Bersih |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2024** | 2.327 | 5.967 unit | Rp 130.883.500 | Rp 3.477.025 | **Rp 127.406.475** |
| **2025** | 2.345 | 6.050 unit | Rp 138.664.000 | Rp 3.662.900 | **Rp 135.001.100** |
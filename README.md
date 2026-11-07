# Analisis Transaksi POS 2024–2025

Notebook ini memuat dua bagian pengolahan dataset transaksi POS: analisis pendapatan tahunan dan manipulasi data dengan Pandas.

Dataset yang digunakan: `paket_a_transaksi_pos_2024_2025.csv`.

## Isi Notebook

### Tugas 1 — Analisis Pendapatan

- Memeriksa duplikat dan nilai kosong.
- Membersihkan format tanggal dan harga.
- Memeriksa kuantitas yang tidak wajar.
- Menghitung pendapatan bersih untuk tahun 2024 dan 2025.
- Menyimpan ringkasan pendapatan dan grafik.

### Tugas 2 — Manipulasi Data dengan Pandas

- Membersihkan harga dan menangani kuantitas negatif.
- Mengisi kode kasir kosong dan memilih kolom dengan `.iloc[]`.
- Menghitung omzet kotor, diskon, dan omzet bersih termasuk PPN 11%.
- Menyaring dan mengurutkan transaksi.
- Membuat ringkasan per gerai dengan `.groupby()`, `.agg()`, dan `.transform()`.

Bagian Tugas 2 membaca ulang CSV asli. Proses ini terpisah dari pembersihan data pada Tugas 1.

## Hasil Analisis Pendapatan

| Tahun | Jumlah Transaksi | Total Barang | Pendapatan Kotor | Total Diskon | Pendapatan Bersih |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2024** | 2.327 | 5.967 unit | Rp 130.883.500 | Rp 3.477.025 | **Rp 127.406.475** |
| **2025** | 2.345 | 6.050 unit | Rp 138.664.000 | Rp 3.662.900 | **Rp 135.001.100** |

## Menjalankan Notebook

Buka `analisis_transaksi_pos.ipynb` melalui Jupyter Notebook atau Google Colab. Letakkan file CSV di direktori yang sama dengan notebook. Paket yang digunakan: `pandas`, `numpy`, dan `matplotlib`.

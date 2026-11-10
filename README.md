# Analisis Transaksi POS 2024–2025

Repository ini berisi tiga notebook pengolahan dan analisis menggunakan dataset transaksi POS yang sama.

## Struktur Direktori

```text
.
├── data/
│   └── paket_a_transaksi_pos_2024_2025.csv
├── notebooks/
│   ├── analisis_transaksi_pos.ipynb
│   ├── tugas_manipulasi_data_pandas.ipynb
│   └── visualisasi_transaksi_pos.ipynb
├── outputs/
│   ├── pendapatan/
│   │   ├── grafik_pendapatan_per_tahun.png
│   │   └── hasil_pendapatan_per_tahun.csv
│   └── visualisasi/
│       └── visualisasi_gabungan_2025.png
└── README.md
```

## Daftar Tugas

### Tugas 1 — Analisis Pendapatan

Notebook: [analisis_transaksi_pos.ipynb](notebooks/analisis_transaksi_pos.ipynb)

- Memeriksa duplikat dan nilai kosong.
- Membersihkan format tanggal dan harga.
- Memeriksa kuantitas yang tidak wajar.
- Menghitung pendapatan bersih tahun 2024 dan 2025.
- Menyimpan ringkasan pendapatan dan grafik ke `outputs/pendapatan/`.

### Tugas 2 — Manipulasi Data dengan Pandas

Notebook: [tugas_manipulasi_data_pandas.ipynb](notebooks/tugas_manipulasi_data_pandas.ipynb)

- Membersihkan format harga dan mengubah tipe data menjadi numerik.
- Mengubah kuantitas negatif menjadi positif.
- Mengisi kode kasir kosong dan memilih kolom dengan `.iloc[]`.
- Menghitung omzet kotor, diskon, omzet bersih, dan PPN 11%.
- Menyaring dan mengurutkan transaksi.
- Membuat laporan gerai dengan `.groupby()`, `.agg()`, dan `.transform()`.

### Tugas 3 — Visualisasi dengan Matplotlib

Notebook: [visualisasi_transaksi_pos.ipynb](notebooks/visualisasi_transaksi_pos.ipynb)

Empat grafik ditampilkan dalam **satu gambar berasio 1:1**, bukan sebagai empat file terpisah:

1. Penjualan bersih per bulan tahun 2025.
2. Sepuluh produk terlaris berdasarkan total unit terjual.
3. Proporsi transaksi selesai, batal, dan retur.
4. Hubungan jumlah pembelian dengan persentase diskon.

## Hasil Visualisasi Tahun 2025

![Visualisasi gabungan transaksi POS 2025](outputs/visualisasi/visualisasi_gabungan_2025.png)

Data dibersihkan dengan menghapus 30 baris duplikat. Setelah pembersihan terdapat 5.000 baris. Dataset mencatat 2.508 transaksi pada tahun 2025: 2.370 `SELESAI`, 89 `BATAL`, dan 49 `RETUR`.

Grafik penjualan dan produk terlaris memakai transaksi `SELESAI` dengan jumlah 1–12 unit. Penjualan bersih dihitung setelah diskon dan sebelum PPN. Batas jumlah tersebut digunakan agar nilai salah input tidak mendominasi grafik.

Grafik proporsi membandingkan transaksi `SELESAI` dengan gabungan `BATAL` dan `RETUR`. Rincian jumlah kedua status tetap ditampilkan secara terpisah.

## Menjalankan Notebook

Buka salah satu notebook di folder `notebooks/` melalui Jupyter Notebook atau Google Colab. Dataset tetap berada di folder `data/`; kode notebook mendeteksi direktori proyek dan menyimpan hasil ke folder `outputs/`.

Paket yang digunakan: `pandas`, `numpy`, dan `matplotlib`.

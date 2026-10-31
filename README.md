# Analisis Pendapatan Transaksi Point of Sales (POS) 2024 - 2025

Mata Kuliah: IT011240 - Pengantar Sains Data  
Topik: Data Cleaning, Penanganan Missing Value, serta Analisis Diskon dan Status Transaksi  
Penyusun: Muhammad Fadhli Rizaldy (NPM: 10124832)  
Kelas: 3KA31  

---

## 1. Ringkasan Tugas

Proyek ini bertujuan untuk mengolah dan menganalisis data riwayat transaksi kasir/POS (*Point of Sales*) dari file `paket_a_transaksi_pos_2024_2025.csv`. Fokus utama dari analisis ini meliputi:
1. Membaca dataset dan mengidentifikasi anomali data.
2. Melakukan penanganan *missing values* secara tepat tanpa menghilangkan integritas data penjualan.
3. Melakukan pembersihan format harga (*decimal comma* dan *thousands dot*) serta standarisasi format tanggal.
4. Menerapkan aturan bisnis (*business rules*) secara cermat mengenai status transaksi dan perhitungan potongan diskon.
5. Menghitung total pendapatan per tahun untuk tahun 2024 dan 2025 secara akurat.
6. Menyimpan hasil pengolahan dan ringkasan agregasi ke dalam format CSV.

---

## 2. Metodologi dan Pembersihan Data (Data Preprocessing)

Dataset mentah berukuran 5.030 baris dan 9 kolom. Berdasarkan hasil audit data, dilakukan langkah-langkah pembersihan sebagai berikut:

### a. Penanganan Data Duplikat
- Terdeteksi sebanyak **30 baris duplikat** identik pada dataset.
- Tindakan: Baris duplikat dihapus menggunakan fungsi `drop_duplicates()`, menyisakan 5.000 baris data transaksi unik.

### b. Penanganan Missing Values
- Terdeteksi sebanyak **260 nilai kosong (*missing value*)** pada kolom `kode_kasir`.
- Tindakan: Kolom `kode_kasir` merupakan data kategorikal identitas petugas kasir. Transaksi tersebut tetap memiliki data produk, harga, kuantitas, tanggal, dan status yang sah. Oleh karena itu, baris tidak dihapus agar tidak mengurangi data omset riil, melainkan diimputasi dengan nilai konstan `'UNKNOWN'`.

### c. Pembersihan Format Harga Satuan (harga_satuan)
- Kolom `harga_satuan` tercatat dalam bentuk teks (*string*) dengan format bervariasi:
  - Format desimal koma (contoh: `7500,00`).
  - Format pemisah ribuan titik (contoh: `13.000` atau `50.500`).
- Tindakan: Dilakukan pembersihan string dengan menghapus akhiran desimal `,00` dan tanda titik pemisah ribuan, kemudian dikonversi menjadi tipe data numerik (*float*).

### d. Penyeragaman Format Tanggal (tanggal)
- Kolom `tanggal` memiliki format campuran (sebagian `YYYY-MM-DD` dan sebagian `DD/MM/YYYY`).
- Tindakan: Dikonversi menggunakan `pd.to_datetime(format='mixed', dayfirst=True)` dan diekstrak menjadi kolom baru `tahun` (2024 dan 2025).

---

## 3. Aturan Bisnis: Status Transaksi dan Perhitungan Diskon

Peringatan utama dalam analisis ini adalah: **"Hati-hati dengan diskon dan status"**.

### a. Status Transaksi
Dataset memiliki 3 variasi status:
1. **SELESAI (4.719 transaksi unik)**: Transaksi penjualan yang sah dan selesai. Barang telah diserahkan dan pembayaran telah diterima. **Hanya status ini yang dihitung sebagai pendapatan toko.**
2. **BATAL (191 transaksi unik)**: Transaksi yang dibatalkan oleh pelanggan atau sistem sebelum pembayaran berhasil. Transaksi ini tidak menghasilkan arus kas masuk sehingga tidak boleh dimasukkan ke dalam pendapatan.
3. **RETUR (90 transaksi unik)**: Barang yang dikembalikan oleh konsumen dan dana dikembalikan (*refund*). Transaksi ini tidak dihitung sebagai omset penjualan.

### b. Perhitungan Diskon Persentase
Kolom `diskon_persen` berisi persentase diskon bernilai 0%, 5%, 10%, 15%, dan 20%. Perhitungan pendapatan bersih (*Net Revenue*) dilakukan secara bertahap:
- `Subtotal Kotor` = `jumlah` * `harga_satuan`
- `Nominal Diskon` = `Subtotal Kotor` * (`diskon_persen` / 100)
- `Pendapatan Bersih` = `Subtotal Kotor` - `Nominal Diskon`

---

## 4. Hasil Output Perhitungan Pendapatan Tahunan

Berikut adalah rekapitulasi pendapatan POS per tahun berdasarkan transaksi yang sah (`status == 'SELESAI'`):

| Tahun | Jumlah Transaksi | Total Barang Terjual | Pendapatan Kotor (Gross) | Total Potongan Diskon | Pendapatan Bersih (Net) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2024** | 2.349 | 14.268 unit | Rp 415.918.000,00 | Rp 29.680.625,00 | **Rp 386.237.375,00** |
| **2025** | 2.370 | 12.499 unit | Rp 265.808.000,00 | Rp 8.722.900,00 | **Rp 257.085.100,00** |
| **TOTAL** | **4.719** | **26.767 unit** | **Rp 681.726.000,00** | **Rp 38.403.525,00** | **Rp 643.322.475,00** |

### Rincian Analisis Finansial:
1. **Tahun 2024**:
   - Total Transaksi Selesai: 2.349 transaksi
   - Total Barang Terjual: 14.268 unit
   - Pendapatan Kotor: Rp 415.918.000,00
   - Potongan Diskon Promosi: Rp 29.680.625,00 (7,14% dari omset kotor)
   - Pendapatan Bersih: **Rp 386.237.375,00**

2. **Tahun 2025**:
   - Total Transaksi Selesai: 2.370 transaksi
   - Total Barang Terjual: 12.499 unit
   - Pendapatan Kotor: Rp 265.808.000,00
   - Potongan Diskon Promosi: Rp 8.722.900,00 (3,28% dari omset kotor)
   - Pendapatan Bersih: **Rp 257.085.100,00**

3. **Total Keseluruhan (2024 - 2025)**:
   - Akumulasi Pendapatan Bersih: **Rp 643.322.475,00**

---

## 5. Validasi: Mengapa Filter Status dan Diskon Wajib Diterapkan?

Tabel di bawah ini menunjukkan perbandingan nilai transaksi jika status tidak disaring:

| Status Transaksi | Tahun | Subtotal Kotor | Potongan Diskon | Pendapatan Bersih | Keterangan |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **SELESAI** | 2024 | Rp 415.918.000,00 | Rp 29.680.625,00 | **Rp 386.237.375,00** | Dihitung sebagai pendapatan riil |
| **SELESAI** | 2025 | Rp 265.808.000,00 | Rp 8.722.900,00 | **Rp 257.085.100,00** | Dihitung sebagai pendapatan riil |
| **BATAL** | 2024 | Rp 4.940.500,00 | Rp 92.650,00 | Rp 4.847.850,00 | Transaksi batal (tidak ada kas) |
| **BATAL** | 2025 | Rp 12.491.000,00 | Rp 537.300,00 | Rp 11.953.700,00 | Transaksi batal (tidak ada kas) |
| **RETUR** | 2024 | Rp 2.175.500,00 | Rp 34.525,00 | Rp 2.140.975,00 | Pengembalian barang (refund) |
| **RETUR** | 2025 | Rp 2.896.000,00 | Rp 63.375,00 | Rp 2.832.625,00 | Pengembalian barang (refund) |

Jika analis tidak memfilter status dan tidak memperhitungkan diskon, angka pendapatan akan mengalami kesalahan fatal (*overstated*) hingga puluhan juta rupiah.

---

## 6. Struktur Berkas Repositori

```text
├── paket_a_transaksi_pos_2024_2025.csv    # Dataset mentah dari dosen
├── analisis_transaksi_pos.ipynb          # Jupyter Notebook lengkap beserta output eksekusi
├── analisis_transaksi_pos.py             # Script Python mandiri
├── hasil_pendapatan_tahunan.csv          # File CSV ringkasan pendapatan tahun 2024 dan 2025
├── transaksi_pos_bersih.csv              # File CSV dataset transaksi yang telah dibersihkan
├── grafik_pendapatan_tahunan.png         # Gambar visualisasi perbandingan pendapatan
└── README.md                             # Dokumentasi laporan hasil analisis
```

---

## 7. Petunjuk Menjalankan Program

### Menjalankan Jupyter Notebook:
```bash
jupyter notebook analisis_transaksi_pos.ipynb
```
Notebook telah dieksekusi terlebih dahulu sehingga seluruh tabel output, ringkasan, dan grafik sudah dapat dilihat langsung di GitHub tanpa harus menjalankan ulang.

### Menjalankan Script Python:
```bash
python analisis_transaksi_pos.py
```
Script akan mencetak ringkasan ke terminal serta memperbarui file output CSV dan file gambar grafik.

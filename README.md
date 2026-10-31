# Analisis Pendapatan Transaksi POS 2024–2025

Repositori ini berisi pengerjaan tugas analisis data transaksi POS (Point of Sales) untuk menghitung total pendapatan tahun 2024 dan 2025 dari dataset `paket_a_transaksi_pos_2024_2025.csv`.

## Ringkasan Pembersihan Data
1. **Data Duplikat**: Menghapus 30 baris duplikat persis.
2. **Missing Value**: Mengisi missing value pada kolom `kode_kasir` dengan `TIDAK_DIKETAHUI` agar data transaksi riil tidak terbuang.
3. **Format Tanggal**: Menyeragamkan format tanggal yang bercampur (YYYY-MM-DD dan DD/MM/YYYY) serta mengekstrak kolom `tahun`.
4. **Format Harga**: Membersihkan karakter titik ribuan (`13.500`) dan koma desimal (`7500,00`) pada `harga_satuan` menjadi numerik.
5. **Validasi Jumlah**: Kuantitas pembelian wajar pada data ritel kasir adalah 1 sampai 12 unit. Nilai negatif (-12 s/d -1) dan nilai ekstrem ribuan (641 s/d 2375) diidentifikasi sebagai salah input/anomali kasir dan dikeluarkan dari perhitungan.
6. **Status Transaksi**: Hanya status `SELESAI` yang diakui sebagai pendapatan sah. Status `BATAL` dan `RETUR` tidak dihitung.
7. **Perhitungan Diskon**: Pendapatan bersih dihitung setelah memotong diskon dengan rumus `jumlah * harga_satuan * (1 - diskon_persen / 100)`.

## Hasil Pendapatan Bersih per Tahun

| Tahun | Jumlah Transaksi | Total Barang | Pendapatan Kotor | Total Diskon | Pendapatan Bersih |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2024** | 2.327 | 5.967 unit | Rp 130.883.500 | Rp 3.477.025 | **Rp 127.406.475** |
| **2025** | 2.345 | 6.050 unit | Rp 138.664.000 | Rp 3.662.900 | **Rp 135.001.100** |

## Perbandingan Berdasarkan Skenario Data

Tabel berikut menunjukkan bukti perubahan nilai jika status transaksi atau anomali data tidak ditangani:

| Skenario | Tahun 2024 | Tahun 2025 | Keterangan |
| :--- | :---: | :---: | :--- |
| Semua status & anomali ikut | Rp 393.226.200 | Rp 271.871.425 | Tidak valid (batal, retur, dan typo ikut terhitung) |
| Hanya SELESAI, anomali ikut | Rp 386.237.375 | Rp 257.085.100 | Masih bias karena anomali kuantitas ribuan belum dibuang |
| **Hanya SELESAI & anomali dibuang (Final)** | **Rp 127.406.475** | **Rp 135.001.100** | **Hasil riil dan akurat** |

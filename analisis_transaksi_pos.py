"""
Program Analisis Data Transaksi POS (Point of Sales) 2024 - 2025
Mata Kuliah: Pengantar Sains Data
Deskripsi:
Program ini melakukan pembacaan dataset transaksi ritel/POS,
penanganan missing values dan data cleaning, analisis status dan diskon,
serta perhitungan pendapatan tahunan (2024 dan 2025) secara akurat.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def format_rupiah(nilai):
    """Fungsi pembantu untuk memformat angka menjadi format mata uang Rupiah."""
    return f"Rp {nilai:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def main():
    print("=" * 70)
    print("PROGRAM ANALISIS PENDAPATAN TRANSAKSI POS (2024 - 2025)")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1. MEMBACA FILE DATASET
    # -------------------------------------------------------------
    file_path = "paket_a_transaksi_pos_2024_2025.csv"
    print(f"\n[1] Membaca file dataset: {file_path}")
    df = pd.read_csv(file_path)

    print(f"    Total data awal : {len(df)} baris, {df.shape[1]} kolom")
    print("\nContoh 5 baris data awal:")
    print(df.head())

    # -------------------------------------------------------------
    # 2. PENGECEKAN DUPLIKAT DAN MISSING VALUE
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[2] PENGECEKAN & PENANGANAN DATA KOTOR (DATA CLEANING)")
    print("=" * 70)

    # Pengecekan data duplikat
    jumlah_duplikat = df.duplicated().sum()
    print(f"\nJumlah data duplikat ditemukan: {jumlah_duplikat} baris")
    if jumlah_duplikat > 0:
        df = df.drop_duplicates().copy()
        print(f"Data duplikat berhasil dihapus. Sisa baris: {len(df)}")

    # Pengecekan missing values
    print("\nPengecekan missing values per kolom:")
    missing_series = df.isnull().sum()
    print(missing_series)

    # Penanganan missing value pada kolom 'kode_kasir'
    # Solusi: Mengisi dengan 'UNKNOWN' agar transaksi riil tidak terbuang
    missing_kasir = df["kode_kasir"].isnull().sum()
    if missing_kasir > 0:
        print(f"\nMenangani {missing_kasir} missing values pada 'kode_kasir'...")
        df["kode_kasir"] = df["kode_kasir"].fillna("UNKNOWN")
        print("Missing value 'kode_kasir' berhasil diisi dengan 'UNKNOWN'.")

    # -------------------------------------------------------------
    # 3. PEMBERSIHAN FORMAT DATA (HARGA SATUAN & TANGGAL)
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[3] PEMBERSIHAN FORMAT HARGA DAN TANGGAL")
    print("=" * 70)

    # Kolom 'harga_satuan' memiliki variasi format string:
    # Contoh: '7500,00' (desimal koma) dan '13.000' (titik ribuan)
    def bersihkan_harga(nilai):
        s = str(nilai).strip()
        if "," in s:
            # Hilangkan desimal ',00' dan titik jika ada
            s = s.split(",")[0].replace(".", "")
        else:
            # Hilangkan pemisah ribuan titik
            s = s.replace(".", "")
        return float(s)

    df["harga_satuan"] = df["harga_satuan"].apply(bersihkan_harga)
    print("Format 'harga_satuan' berhasil diubah menjadi tipe numerik (float).")

    # Konversi kolom 'tanggal' ke format datetime
    df["tanggal"] = pd.to_datetime(df["tanggal"], format="mixed", dayfirst=True)
    df["tahun"] = df["tanggal"].dt.year
    print("Kolom 'tanggal' berhasil dikonversi. Kolom 'tahun' berhasil diekstrak.")

    # -------------------------------------------------------------
    # 4. ANALISIS ATURAN BISNIS: STATUS TRANSAKSI & DISKON
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[4] ANALISIS STATUS TRANSAKSI & PERHITUNGAN DISKON")
    print("=" * 70)

    print("\nDistribusi Status Transaksi:")
    print(df["status"].value_counts())

    print("\nCatatan Aturan Bisnis:")
    print("1. Status 'SELESAI' adalah transaksi sah yang menghasilkan pendapatan.")
    print("2. Status 'BATAL' dibatalkan sebelum selesai sehingga TIDAK dihitung.")
    print("3. Status 'RETUR' adalah pengembalian barang sehingga TIDAK dihitung sebagai omset.")
    print("4. Diskon (%): Pendapatan bersih dihitung setelah memotong diskon.")

    # Menghitung subtotal kotor, nominal diskon, dan pendapatan bersih
    # Rumus:
    # - Subtotal Kotor = jumlah * harga_satuan
    # - Nominal Diskon = Subtotal Kotor * (diskon_persen / 100)
    # - Pendapatan Bersih = Subtotal Kotor - Nominal Diskon
    df["subtotal_kotor"] = df["jumlah"] * df["harga_satuan"]
    df["nominal_diskon"] = df["subtotal_kotor"] * (df["diskon_persen"] / 100.0)
    df["pendapatan_bersih"] = df["subtotal_kotor"] - df["nominal_diskon"]

    # Filter transaksi yang valid untuk pendapatan (Status SELESAI)
    df_valid = df[df["status"] == "SELESAI"].copy()

    # -------------------------------------------------------------
    # 5. PERHITUNGAN JUMLAH PENDAPATAN PER TAHUN (2024 & 2025)
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[5] HASIL PERHITUNGAN PENDAPATAN PER TAHUN")
    print("=" * 70)

    # Agregasi per tahun
    ringkasan_tahunan = df_valid.groupby("tahun").agg(
        total_transaksi=("id_transaksi", "count"),
        total_barang=("jumlah", "sum"),
        pendapatan_kotor=("subtotal_kotor", "sum"),
        total_diskon=("nominal_diskon", "sum"),
        pendapatan_bersih=("pendapatan_bersih", "sum")
    ).reset_index()

    # Tampilan tabel terminal yang rapi
    print("\nRingkasan Pendapatan Tahunan:")
    print("-" * 75)
    print(f"{'Tahun':<8} | {'Transaksi':<10} | {'Qty Barang':<12} | {'Pendapatan Bersih (Net)':<25}")
    print("-" * 75)
    for _, row in ringkasan_tahunan.iterrows():
        th = int(row["tahun"])
        trx = int(row["total_transaksi"])
        qty = int(row["total_barang"])
        bersih_str = format_rupiah(row["pendapatan_bersih"])
        print(f"{th:<8} | {trx:<10,d} | {qty:<12,d} | {bersih_str:<25}")
    print("-" * 75)

    # Rincian per tahun secara detail
    print("\nRincian Detail Finansial per Tahun:")
    for _, row in ringkasan_tahunan.iterrows():
        th = int(row["tahun"])
        print(f"\n--- TAHUN {th} ---")
        print(f"  Jumlah Transaksi Selesai : {int(row['total_transaksi']):,} transaksi")
        print(f"  Total Barang Terjual     : {int(row['total_barang']):,} unit")
        print(f"  Pendapatan Kotor (Gross) : {format_rupiah(row['pendapatan_kotor'])}")
        print(f"  Total Potongan Diskon    : {format_rupiah(row['total_diskon'])}")
        print(f"  Pendapatan Bersih (Net)  : {format_rupiah(row['pendapatan_bersih'])}")

    total_pendapatan_all = ringkasan_tahunan["pendapatan_bersih"].sum()
    print(f"\nTOTAL PENDAPATAN BERSIH (2024 + 2025): {format_rupiah(total_pendapatan_all)}")

    # -------------------------------------------------------------
    # 6. MENYIMPAN HASIL OUTPUT KE FILE CSV
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[6] MENYIMPAN HASIL KE FILE CSV")
    print("=" * 70)

    # File 1: Ringkasan tahunan
    output_summary_csv = "hasil_pendapatan_tahunan.csv"
    ringkasan_tahunan.to_csv(output_summary_csv, index=False)
    print(f"File ringkasan berhasil disimpan: {output_summary_csv}")

    # File 2: Dataset transaksi yang sudah bersih & terhitung
    output_detail_csv = "transaksi_pos_bersih.csv"
    df.to_csv(output_detail_csv, index=False)
    print(f"File transaksi bersih berhasil disimpan: {output_detail_csv}")

    # -------------------------------------------------------------
    # 7. VISUALISASI PENDAPATAN TAHUNAN
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[7] MEMBUAT GRAFIK VISUALISASI")
    print("=" * 70)

    plt.figure(figsize=(8, 5))
    tahun_labels = [str(int(t)) for t in ringkasan_tahunan["tahun"]]
    pendapatan_juta = ringkasan_tahunan["pendapatan_bersih"] / 1_000_000

    bars = plt.bar(tahun_labels, pendapatan_juta, color=["#1f77b4", "#2ca02c"], width=0.5)
    plt.title("Perbandingan Pendapatan Bersih POS (2024 vs 2025)", fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Tahun", fontsize=11)
    plt.ylabel("Pendapatan Bersih (Juta Rupiah)", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Label angka di atas batang
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + 5,
                 f"Rp {height:,.1f} Juta",
                 ha="center", va="bottom", fontsize=10, fontweight="bold")

    plt.ylim(0, max(pendapatan_juta) * 1.18)
    chart_file = "grafik_pendapatan_tahunan.png"
    plt.tight_layout()
    plt.savefig(chart_file, dpi=300)
    plt.close()
    print(f"Grafik visualisasi berhasil disimpan: {chart_file}")

    print("\nSemua proses analisis selesai dengan sukses.")


if __name__ == "__main__":
    main()

# Program untuk menambah data ke dalam list dan menghitung nilai akhir

data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

    # Simpan ke list
    data_mahasiswa.append({
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    # Tanya apakah ingin menambah data lagi
    lanjut = input("\nTambah data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Tampilkan daftar data mahasiswa
print("\nDaftar Nilai Mahasiswa")
print("=" * 50)
print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(
    "Nama", "Tugas", "UTS", "UAS", "Akhir"))
print("=" * 50)

for mhs in data_mahasiswa:
    print("{:<15} {:<10} {:<10} {:<10} {:<10.2f}".format(
        mhs['Nama'], mhs['Tugas'], mhs['UTS'], mhs['UAS'], mhs['Nilai Akhir']))

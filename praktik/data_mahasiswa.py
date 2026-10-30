mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if not data:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


print("=== DATA MAHASISWA ===")
for nim, info in mahasiswa.items():
    print(f"{nim}: {info}")


print("\n=== CARI MAHASISWA ===")
nim_cari = "A003"
hasil = cari_mahasiswa(mahasiswa, nim_cari)

if hasil:
    print(f"Data mahasiswa {nim_cari}: {hasil}")
else:
    print("Data mahasiswa tidak ditemukan.")


print("\n=== TAMBAH MAHASISWA ===")
mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Mahasiswa berhasil ditambahkan.")
print(f"A006: {mahasiswa['A006']}")


print("\n=== UPDATE NILAI MAHASISWA ===")
mahasiswa["A002"]["nilai"] = 82

print("Nilai mahasiswa A002 berhasil diperbarui.")
print(f"Data terbaru: {mahasiswa['A002']}")


print("\n=== SELURUH DATA MAHASISWA TERBARU ===")
for nim, info in mahasiswa.items():
    print(f"NIM: {nim}")
    print(f"Nama: {info['nama']}")
    print(f"Kelas: {info['kelas']}")
    print(f"Nilai: {info['nilai']}")
    print("-" * 30)


print("\n=== RATA-RATA NILAI MAHASISWA ===")
rata_rata = rata_rata_nilai(mahasiswa)
print(f"Rata-rata nilai: {rata_rata:.2f}")
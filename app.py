print("SLIP GAJI PT DINGIN DAMAI")
print("=" * 40)

nama = input("Nama karyawan : ").upper()
gol_jabatan = int(input("golongan jabatan [1/2/3] : "))
pendidikan = input("Pendidikan [SMA/D1/D3/S1]: ").upper()
jml_jam_kerja = int(input("jumlah jam kerja : "))
gaji_pokok = 300000

print("=" * 40)

# mengitung jumlah bonus berdasarkan jabatan
if gol_jabatan == 1:
    tunjangan_jabatan = int(0.05 * gaji_pokok)
elif gol_jabatan == 2:
    tunjangan_jabatan = int(0.10 * gaji_pokok)
elif gol_jabatan == 3:
    tunjangan_jabatan = int(0.15 * gaji_pokok)
else:
    tunjangan_jabatan = 0

# bonus berdasarkan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = int(0.025 * gaji_pokok)
elif pendidikan == "D1":
    tunjangan_pendidikan = int(0.05 * gaji_pokok)
elif pendidikan == "D3":
    tunjangan_pendidikan = int(0.2 * gaji_pokok)
elif pendidikan == "S1":
    tunjangan_pendidikan = int(0.3 * gaji_pokok)
else:
    tunjangan_pendidikan = 0

if jml_jam_kerja > 8:
    lembur = (jml_jam_kerja - 8) * 3500
else:
    lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

print(f"gaji yang diterima oleh {nama}")
print(f"gaji pokok : {gaji_pokok:,}")
print(f"tunjangan jabatan : {tunjangan_jabatan:,}")
print(f"tunjangan pendidikan : {tunjangan_pendidikan:,}")
print(f"honor lembur : {lembur:,}")
print(f"total gaji : {total_gaji:,}")

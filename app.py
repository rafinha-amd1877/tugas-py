print("SLIP GAJI PT DINGIN DAMAI")
print("=" * 40)

nama = input("Nama karyawan : ")
gol_jabatan = int(input("golongan jabatan [1/2/3] : "))
pendidikan = input("Pendidikan [SMA/D1/D3/S1]: ".upper())
jml_jam_kerja = int(input("jumlah jam kerja : "))
gaji_pokok = 300000

upperName = nama.upper()
upperPend = pendidikan.upper()

print("=" * 40)

# mengitung jumlah bonus berdasarkan jabatan
if gol_jabatan == 1:
    tunjangan_jabatan = 0.05 * 300000
elif gol_jabatan == 2:
    tunjangan_jabatan = 0.10 * 300000
elif gol_jabatan == 3:
    tunjangan_jabatan = 0.15 * 300000
else:
    tunjangan_jabatan = 0

# bonus berdasarkan pendidikan
if upperPend == "SMA":
    tunjangan_pendidikan = 0.025 * 300000
elif upperPend == "D1":
    tunjangan_pendidikan = 0.05 * 300000
elif upperPend == "D3":
    tunjangan_pendidkan = 0.2 * 300000
elif upperPend == "S1":
    tunjangan_pendidikan = 0.3 * 300000
else:
    tunjangan_pendidikan = 0

if jml_jam_kerja > 8:
    lembur = (jml_jam_kerja - 8) * 3500
else:
    lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

print(f"gaji yang diterima oleh {nama}")
print(f"tunjangan jabatan : {tunjangan_jabatan:,}")
print(f"tunjangan pendidikan : {tunjangan_pendidikan:,}")
print(f"honor lembur : {lembur:,}")
print(f"total gaji : {total_gaji:,}")

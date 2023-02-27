import json

# menerima input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang = "))

# membuat list kosong untuk menyimpan data barang
daftar_barang = []

# melakukan iterasi sebanyak jumlah barang untuk menerima input nama dan harga barang
for i in range(jumlah_barang):
    nama_barang = input(f"Nama barang {i+1} = ")
    harga_barang = int(input(f"Harga barang {i+1} = "))
    # menambahkan data barang ke dalam list
    daftar_barang.append({"nama": nama_barang, "harga": harga_barang})

# menghitung total harga dari seluruh barang
total_harga = sum([barang["harga"] for barang in daftar_barang])

# membuat dictionary untuk menyimpan total dan daftar barang
data = {"total": total_harga, "barang": daftar_barang}

# menyimpan data dalam file JSON
with open("data_barang.json", "w") as file:
    json.dump(data,file)
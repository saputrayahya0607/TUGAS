data = []
def insert():

    nama = input('nama barang = ')
    stok = int(input('stok barang = '))
    data_baru = {'nama' : nama,'stok' : stok}
    data.append(data_baru)

def view_data():
    if not data:
       print('='*6,'Stok barang Kosong','='*6)
    else:    
     for i in data :
        print('-',i['nama'],i['stok'])
def hapus_data():
    id = int(input('masukan data yang ke berapa'))
    del data[id]
    print('hapus data berhasil')

def edit_data():
    view_data() 
 
    id = int(input('Masukan nomor data yang ingin diedit: '))
    if 0 <= id and id < len(data):
        print(f'Edit data untuk {data[id]["nama"]}')
        new_nama = input('Nama baru: ')
        new_stok = int(input('Stok baru: '))
        data[id]['nama'] = new_nama
        data[id]['stok'] = new_stok
        print(f'Data {id} berhasil diperbarui!')
    else:
         print('Nomor data tidak valid!')
def jumlah_data():
    print(f'Total data: {len(data)}')


def cari_data():
    nama_cari = input('Masukkan nama barang yang ingin dicari: ')
    for  item in (data):
         if nama_cari.lower() in item["nama"].lower():
            print(f'- Nama: {item["nama"]} Stok: {item["stok"]}')
         else :
          print('Data tidak ditemukan.')
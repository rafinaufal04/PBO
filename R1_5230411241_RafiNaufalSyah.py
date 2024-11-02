class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info(self):
        return f"Pegawai: {self.nama} (NIK: {self.nik}), Alamat: {self.alamat}"

class Produk:
    def __init__(self, kode_produk, nama_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

    def tampilkan_info(self):
        return f"{self.kode_produk}: {self.nama_produk} - Rp {self.harga}"

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, harga)

class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, harga)

class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, harga)

class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_dibeli = []
        self.total_harga = 0

    def tambah_produk(self, produk, jumlah):
        self.produk_dibeli.append((produk, jumlah))
        self.total_harga += produk.harga * jumlah

    def tampilkan_transaksi(self):
        hasil = f"Transaksi No: {self.no_transaksi}\n{self.pegawai.tampilkan_info()}\n"
        hasil += "Produk yang dibeli:\n"
        for produk, jumlah in self.produk_dibeli:
            hasil += f"- {produk.nama_produk} (x{jumlah}) = Rp {produk.harga * jumlah}\n"
        hasil += f"Total: Rp {self.total_harga}"
        return hasil

# Daftar pegawai, produk, dan transaksi
pegawai_list = []
produk_list = []
transaksi_list = []

# Fungsi CRUD untuk Pegawai
def tambah_pegawai():
    nik = input("Masukkan NIK Pegawai: ")
    nama = input("Masukkan Nama Pegawai: ")
    alamat = input("Masukkan Alamat Pegawai: ")
    pegawai = Pegawai(nik, nama, alamat)
    pegawai_list.append(pegawai)
    print("Pegawai berhasil ditambahkan!")

def tampilkan_pegawai():
    if not pegawai_list:
        print("Tidak ada pegawai.")
    else:
        for pegawai in pegawai_list:
            print(pegawai.tampilkan_info())

# Fungsi CRUD untuk Produk
def tambah_produk():
    tipe = input("Masukkan tipe produk (Snack/Makanan/Minuman): ").lower()
    kode_produk = input("Masukkan kode produk: ")
    nama_produk = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga: "))
    
    if tipe == "snack":
        produk = Snack(kode_produk, nama_produk, harga)
    elif tipe == "makanan":
        produk = Makanan(kode_produk, nama_produk, harga)
    elif tipe == "minuman":
        produk = Minuman(kode_produk, nama_produk, harga)
    else:
        print("Tipe produk tidak valid!")
        return
    
    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Tidak ada produk.")
    else:
        for produk in produk_list:
            print(produk.tampilkan_info())

# Fungsi CRUD untuk Transaksi
def tambah_transaksi():
    if not pegawai_list:
        print("Belum ada pegawai yang terdaftar.")
        return
    
    no_transaksi = input("Masukkan nomor transaksi: ")
    tampilkan_pegawai()
    pegawai_nik = input("Masukkan NIK pegawai yang melakukan transaksi: ")
    
    pegawai = next((p for p in pegawai_list if p.nik == pegawai_nik), None)
    if not pegawai:
        print("Pegawai tidak ditemukan!")
        return
    
    transaksi = Transaksi(no_transaksi, pegawai)
    
    while True:
        tampilkan_produk()
        kode_produk = input("Masukkan kode produk (atau ketik 'selesai' untuk selesai): ")
        if kode_produk.lower() == 'selesai':
            break
        
        produk = next((p for p in produk_list if p.kode_produk == kode_produk), None)
        if not produk:
            print("Produk tidak ditemukan!")
            continue

        jumlah = int(input("Masukkan jumlah produk: "))
        transaksi.tambah_produk(produk, jumlah)
    
    transaksi_list.append(transaksi)
    print("Transaksi berhasil ditambahkan!")

def tampilkan_transaksi():
    if not transaksi_list:
        print("Tidak ada transaksi.")
    else:
        for transaksi in transaksi_list:
            print(transaksi.tampilkan_transaksi())

# Cetak Struk
def cetak_struk():
    no_transaksi = input("Masukkan nomor transaksi yang akan dicetak struknya: ")
    transaksi = next((t for t in transaksi_list if t.no_transaksi == no_transaksi), None)
    if transaksi:
        print("\n=== STRUK PEMBELIAN ===")
        print(transaksi.tampilkan_transaksi())
        print("=======================")
    else:
        print("Transaksi tidak ditemukan!")

# Menu Utama
def menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Lihat Produk")
        print("2. Lihat Transaksi")
        print("3. Lihat Pegawai")
        print("4. Exit Program")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            while True:
                print("\n--- MENU PRODUK ---")
                print("1. Tambah Produk")
                print("2. Tampilkan Produk")
                print("3. Kembali ke Menu Utama")
                pilihan_produk = input("Pilih menu produk: ")
                
                if pilihan_produk == "1":
                    tambah_produk()
                elif pilihan_produk == "2":
                    tampilkan_produk()
                elif pilihan_produk == "3":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "2":
            while True:
                print("\n--- MENU TRANSAKSI ---")
                print("1. Tambah Transaksi")
                print("2. Tampilkan Transaksi")
                print("3. Cetak Struk")
                print("4. Kembali ke Menu Utama")
                pilihan_transaksi = input("Pilih menu transaksi: ")
                
                if pilihan_transaksi == "1":
                    tambah_transaksi()
                elif pilihan_transaksi == "2":
                    tampilkan_transaksi()
                elif pilihan_transaksi == "3":
                    cetak_struk()
                elif pilihan_transaksi == "4":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "3":
            while True:
                print("\n--- MENU PEGAWAI ---")
                print("1. Tambah Pegawai")
                print("2. Tampilkan Pegawai")
                print("3. Kembali ke Menu Utama")
                pilihan_pegawai = input("Pilih menu pegawai: ")
                
                if pilihan_pegawai == "1":
                    tambah_pegawai()
                elif pilihan_pegawai == "2":
                    tampilkan_pegawai()
                elif pilihan_pegawai == "3":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif pilihan == "4":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid!")

# Menjalankan menu
menu()
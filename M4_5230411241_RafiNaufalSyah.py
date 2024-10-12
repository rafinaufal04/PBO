class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama  
        self.__ktp = ktp  
        self._limit_pinjaman = limit_pinjaman 

    def tampilkan(self):
        return f"Nama: {self.nama}, Limit Pinjaman: {self._limit_pinjaman}"

    def get_detail(self):
        return f"Nama: {self.nama}, KTP: {self.__ktp}, Limit Pinjaman: {self._limit_pinjaman}"

    def get_ktp(self):
        return self.__ktp

class Pinjaman:
    def __init__(self, debitur, jumlah_pinjaman, bunga, bulan):
        if jumlah_pinjaman > debitur._limit_pinjaman:
            raise ValueError("Pinjaman melebihi limit!")
        self.debitur = debitur
        self.jumlah_pinjaman = jumlah_pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran_pokok = self.jumlah_pinjaman * (self.bunga / 100)
        self.angsuran_bulanan = self.angsuran_pokok / self.bulan
        self.total_angsuran = self.angsuran_pokok + self.angsuran_bulanan

    def tampilkan_pinjaman(self):
        return (f"Nama: {self.debitur.nama}, Pinjaman: {self.jumlah_pinjaman}, "
                f"Bunga: {self.bunga}%, Bulan: {self.bulan}, "
                f"Angsuran Bulanan: {self.angsuran_bulanan:.2f}")

class ManajemenDebitur:
    def __init__(self):
        self.data_debitur = []

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        for debitur in self.data_debitur:
            if debitur.get_ktp() == ktp:
                print("Validasi Gagal: KTP sudah ada!")
                return
        debitur_baru = Debitur(nama, ktp, limit_pinjaman)
        self.data_debitur.append(debitur_baru)
        print("Debitur berhasil ditambahkan.")

    def tampilkan_debitur(self):
        if not self.data_debitur:
            print("Belum ada debitur.")
        for debitur in self.data_debitur:
            print(debitur.tampilkan())

    def cari_debitur(self, nama):
        for debitur in self.data_debitur:
            if debitur.nama == nama:
                print(debitur.get_detail())
                return debitur
        print("Debitur tidak ditemukan.")
        return None
    
class ManajemenPinjaman:
    def __init__(self):
        self.data_pinjaman = []

    def tambah_pinjaman(self, manajemen_debitur, nama_debitur, jumlah_pinjaman, bunga, bulan):
        debitur = manajemen_debitur.cari_debitur(nama_debitur)
        if debitur is None:
            print("Debitur tidak ditemukan!")
            return
        try:
            pinjaman_baru = Pinjaman(debitur, jumlah_pinjaman, bunga, bulan)
            self.data_pinjaman.append(pinjaman_baru)
            print("Pinjaman berhasil ditambahkan.")
        except ValueError as e:
            print(e)

    def tampilkan_pinjaman(self):
        if not self.data_pinjaman:
            print("Belum ada pinjaman.")
        for pinjaman in self.data_pinjaman:
            print(pinjaman.tampilkan_pinjaman())

def menu():
    manajemen_debitur = ManajemenDebitur()
    manajemen_pinjaman = ManajemenPinjaman()

    while True:
        print("\n===== MENU PINJOL =====")
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("3. Kembali")
        print("=======================")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            sub_menu_debitur(manajemen_debitur)
        elif pilihan == "2":
            sub_menu_pinjaman(manajemen_debitur, manajemen_pinjaman)
        elif pilihan == "3":
            print("KTerimakasih sudah pinjol.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def sub_menu_debitur(manajemen_debitur):
    while True:
        print("\n===== KELOLA DEBITUR =====")
        print("1. Tambah Debitur")
        print("2. Tampilkan Semua Debitur")
        print("3. Cari Debitur")
        print("4. Kembali ke menu utama")
        print("=======================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama debitur: ")
            ktp = input("Masukkan KTP debitur: ")
            limit_pinjaman = float(input("Masukkan limit pinjaman: "))
            manajemen_debitur.tambah_debitur(nama, ktp, limit_pinjaman)

        elif pilihan == "2":
            manajemen_debitur.tampilkan_debitur()

        elif pilihan == "3":
            nama = input("Masukkan nama debitur yang ingin dicari: ")
            manajemen_debitur.cari_debitur(nama)

        elif pilihan == "4":
            print("Kembali ke Menu Utama.")
            break

        else:
            print("Pilihan tidak valid, Silakan coba lagi.")

def sub_menu_pinjaman(manajemen_debitur, manajemen_pinjaman):
    while True:

        print("\n===== Kelola Pinjaman =====")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Semua Pinjaman")
        print("3. Kembali ke menu utama")
        print("==============================")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama_debitur = input("Masukkan nama debitur: ")
            jumlah_pinjaman = float(input("Masukkan jumlah pinjaman: "))
            bunga = float(input("Masukkan persen bunga (%): "))
            bulan = int(input("Masukkan jumlah bulan cicilan: "))
            manajemen_pinjaman.tambah_pinjaman(manajemen_debitur, nama_debitur, jumlah_pinjaman, bunga, bulan)

        elif pilihan == "2":
            manajemen_pinjaman.tampilkan_pinjaman()

        elif pilihan == "3":
            print("Kembali ke Menu Utama.")
            break

        else:
            print("Pilihan tidak valid, Silakan coba lagi.")

menu()
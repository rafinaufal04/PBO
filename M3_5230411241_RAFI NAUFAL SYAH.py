class DaftarMenu:
    def __init__(self):
        self.makanan = []
        self.minuman = []

    def daftar_makanan(self):
        if not self.makanan:
            print("Belum ada makanan yang tersedia.")
        else:
            print("\n=== Daftar Makanan ===")
            print("{:<5} {:<30} {:>15}".format("No", "Nama Makanan", "Harga (Rp)"))
            print("-" * 50)
            for idx, item in enumerate(self.makanan, start=1):
                print("{:<5} {:<30} {:>15,}".format(idx, item['nama'], item['harga']))
    
    def daftar_minuman(self):
        if not self.minuman:
            print("Belum ada minuman yang tersedia.")
        else:
            print("\n=== Daftar Minuman ===")
            print("{:<5} {:<30} {:>15}".format("No", "Nama Minuman", "Harga (Rp)"))
            print("-" * 50)
            for idx, item in enumerate(self.minuman, start=1):
                print("{:<5} {:<30} {:>15,}".format(idx, item['nama'], item['harga']))

    def tambah_makanan(self, makanan_baru, harga_makanan):
        self.makanan.append({'nama': makanan_baru, 'harga': harga_makanan})
        print(f"Makanan '{makanan_baru}' dengan harga Rp {harga_makanan:,} telah ditambahkan.")

    def tambah_minuman(self, minuman_baru, harga_minuman):
        self.minuman.append({'nama': minuman_baru, 'harga': harga_minuman})
        print(f"Minuman '{minuman_baru}' dengan harga Rp {harga_minuman:,} telah ditambahkan.")

    def tambah_menu(self):
        while True:
            print("\n=== Tambah Menu ===")
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")
            print("3. Kembali ke Menu Utama")
            
            pilihan_menu = input("Masukkan Pilihan: ")

            if pilihan_menu == '1':
                makanan_baru = input("Masukkan nama makanan: ")
                if not makanan_baru:
                    print("Nama makanan tidak boleh kosong.")
                    continue
                while True:
                    try:
                        harga_makanan = int(input("Masukkan harga makanan (Rp): "))
                        if harga_makanan < 0:
                            print("Harga tidak Valid. Silakan masukkan kembali.")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")
                self.tambah_makanan(makanan_baru, harga_makanan)
            elif pilihan_menu == '2':
                minuman_baru = input("Masukkan nama minuman: ")
                if not minuman_baru:
                    print("Nama minuman tidak boleh kosong.")
                    continue
                while True:
                    try:
                        harga_minuman = int(input("Masukkan harga minuman (Rp): "))
                        if harga_minuman < 0:
                            print("Harga tidak valid. Silakan masukkan kembali.")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka.")
                self.tambah_minuman(minuman_baru, harga_minuman)
            elif pilihan_menu == '3':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    daftar_menu = DaftarMenu()
    
    while True:
        print("\n=== Daftar Menu ===")
        print("1. Daftar Makanan")
        print("2. Daftar Minuman")
        print("3. Tambah Menu")
        print("0. Keluar Program")
        
        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            daftar_menu.daftar_makanan()
        elif pilihan == '2':
            daftar_menu.daftar_minuman()
        elif pilihan == '3':
            daftar_menu.tambah_menu()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
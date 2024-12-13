import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="penjualan"
)

cur = conn.cursor()


# cur.execute("""
#     CREATE TABLE pegawai (
#     nik VARCHAR(20) PRIMARY KEY,
#     nama_pegawai VARCHAR(100),
#     alamat_pegawai VARCHAR(255))
#     """)

# cur.execute("""
#     CREATE TABLE transaksi (
#     no_transaksi VARCHAR(20) PRIMARY KEY,
#     detail_transaksi TEXT)
#     """)

# cur.execute("""
#     CREATE TABLE produk (
#     kode_produk VARCHAR(20) PRIMARY KEY,
#     nama_produk VARCHAR(100),
#     jenis_produk VARCHAR(100),
#     harga_produk INT)
#     """)

# cur.execute("""
#     CREATE TABLE struk (
#     no_struk VARCHAR(20) PRIMARY KEY,
#     nama_pegawai VARCHAR(50),
#     no_transaksi VARCHAR(20),
#     nama_produk VARCHAR(100),
#     jumlah_produk INT,
#     total_harga INT)
#     """)


# cur.execute("""
#         ALTER TABLE struk
#         ADD FOREIGN KEY (nama_pegawai) REFERENCES pegawai(nik),
#         ADD FOREIGN KEY (no_transaksi) REFERENCES transaksi(no_transaksi),
#         ADD FOREIGN KEY (nama_produk) REFERENCES produk(kode_produk)
#     """)
# conn.commit()

def main_menu():
    print("\n=== Sistem Manajemen Penjualan ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    
    try:
        return int(input("Pilih menu: "))
    except ValueError:
        return 0

def tambah_data(cursor, conn):
    print("\n-- Tambah Data --")
    print("1. Pegawai")
    print("2. Produk")
    print("3. Transaksi")
    print("4. Struk")
    choice = int(input("Pilih tabel: "))

    if choice == 1:
        nik = input("Masukkan NIK: ")
        nama = input("Masukkan Nama Pegawai: ")
        alamat = input("Masukkan Alamat Pegawai: ")
        cursor.execute("INSERT INTO pegawai (nik, nama_pegawai, alamat_pegawai) VALUES (%s, %s, %s)", (nik, nama, alamat))
        conn.commit()
        print("Data pegawai berhasil ditambahkan.")
    elif choice == 2:
        kode = input("Masukkan Kode Produk: ")
        nama = input("Masukkan Nama Produk: ")
        jenis = input("Masukkan Jenis Produk: ")
        harga = int(input("Masukkan Harga Produk: "))
        cursor.execute("INSERT INTO produk (kode_produk, nama_produk, jenis_produk, harga_produk) VALUES (%s, %s, %s, %s)", (kode, nama, jenis, harga))
        conn.commit()
        print("Data produk berhasil ditambahkan.")
    elif choice == 3:
        no_transaksi = input("Masukkan No Transaksi: ")
        detail = input("Masukkan Detail Transaksi: ")
        cursor.execute("INSERT INTO transaksi (no_transaksi, detail_transaksi) VALUES (%s, %s)", (no_transaksi, detail))
        conn.commit()
        print("Data transaksi berhasil ditambahkan.")
    elif choice == 4:
        no_transaksi = input("Masukkan No Transaksi: ")
        nama_pegawai = input("Masukkan NIK Pegawai: ")

        # Verifikasi pegawai
        cursor.execute("SELECT nik FROM pegawai WHERE nik = %s", (nama_pegawai,))
        pegawai = cursor.fetchone()

        if pegawai is None:
            print("Pegawai tidak ditemukan.")
            return 

        nama_produk = input("Masukkan Kode Produk: ")

        # Verifikasi produk
        cursor.execute("SELECT harga_produk FROM produk WHERE kode_produk = %s", (nama_produk,))
        produk = cursor.fetchone()

        if produk is None:
            print("Produk tidak ditemukan.")
            return

        harga_produk = produk[0]
        jumlah = int(input("Masukkan Jumlah Produk: "))
        total = jumlah * harga_produk

        try:
            cursor.execute(
                "INSERT INTO struk (no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga) VALUES (%s, %s, %s, %s, %s)",
                (no_transaksi, nama_pegawai, nama_produk, jumlah, total)
            )
            conn.commit()
            print(f"Data struk berhasil ditambahkan. Total Harga: {total}")
        except mysql.connector.Error as err:
            print(f"Error saat menambahkan data: {err}")


def tampilkan_data(cursor):
    print("\n-- Tampilkan Data --")
    print("1. Pegawai")
    print("2. Produk")
    print("3. Transaksi")
    print("4. Struk")
    choice = int(input("Pilih tabel: "))

    tabel = {1: "pegawai", 2: "produk", 3: "transaksi", 4: "struk"}.get(choice, None)
    if tabel:
        cursor.execute(f"SELECT * FROM {tabel}")
        for row in cursor.fetchall():
            print(row)
    else:
        print("Pilihan tidak valid.")

def ubah_data(cursor, conn):
    print("\n-- Ubah Data --")
    print("1. Pegawai")
    print("2. Produk")
    print("3. Transaksi")
    print("4. Struk")
    choice = int(input("Pilih tabel: "))

    if choice == 1:
        nik = input("Masukkan NIK pegawai yang akan diubah: ")
        nama = input("Masukkan Nama Pegawai baru: ")
        alamat = input("Masukkan Alamat Pegawai baru: ")
        cursor.execute("UPDATE pegawai SET nama_pegawai=%s, alamat_pegawai=%s WHERE nik=%s", (nama, alamat, nik))
        conn.commit()
        print("Data pegawai berhasil diubah.")
    elif choice == 2:
        kode = input("Masukkan Kode Produk yang akan diubah: ")
        nama = input("Masukkan Nama Produk baru: ")
        jenis = input("Masukkan Jenis Produk baru: ")
        harga = int(input("Masukkan Harga Produk baru: "))
        cursor.execute("UPDATE produk SET nama_produk=%s, jenis_produk=%s, harga_produk=%s WHERE kode_produk=%s", (nama, jenis, harga, kode))
        conn.commit()
        print("Data produk berhasil diubah.")
    elif choice == 3:
        no_transaksi = input("Masukkan No Transaksi yang akan diubah: ")
        detail = input("Masukkan Detail Transaksi baru: ")
        cursor.execute("UPDATE transaksi SET detail_transaksi=%s WHERE no_transaksi=%s", (detail, no_transaksi))
        conn.commit()
        print("Data transaksi berhasil diubah.")
    elif choice == 4:
        no_transaksi = input("Masukkan No Transaksi yang akan diubah: ")
        nama_pegawai = input("Masukkan NIK Pegawai baru: ")
        nama_produk = input("Masukkan Kode Produk baru: ")
        jumlah = int(input("Masukkan Jumlah Produk baru: "))

        # Dapatkan harga produk dari tabel produk
        cursor.execute("SELECT harga_produk FROM produk WHERE kode_produk = %s", (nama_produk,))
        produk = cursor.fetchone()

        if produk is None:
            print("Error: Produk dengan kode tersebut tidak ditemukan.")
            return  # Hentikan jika produk tidak ditemukan

        harga_produk = produk[0]
        total = jumlah * harga_produk  # Hitung total harga secara otomatis

        # Update data di tabel struk
        cursor.execute(
            "UPDATE struk SET nama_pegawai=%s, nama_produk=%s, jumlah_produk=%s, total_harga=%s WHERE no_transaksi=%s",
            (nama_pegawai, nama_produk, jumlah, total, no_transaksi)
        )
        conn.commit()
        print(f"Data struk berhasil diubah. Total Harga otomatis dihitung: {total}")
    else:
        print("Pilihan tidak valid.")


def hapus_data(cursor, conn):
    print("\n-- Hapus Data --")
    print("1. Pegawai")
    print("2. Produk")
    print("3. Transaksi")
    print("4. Struk")
    choice = int(input("Pilih tabel: "))

    tabel = {1: "pegawai", 2: "produk", 3: "transaksi", 4: "struk"}.get(choice, None)
    if tabel:
        id_field = input(f"Masukkan ID (atau NIK/No Transaksi/Kode Produk) yang akan dihapus dari tabel {tabel}: ")
        primary_key = {"pegawai": "nik", "produk": "kode_produk", "transaksi": "no_transaksi", "struk": "no_struk"}[tabel]

        # Jika tabel adalah 'pegawai', hapus dependensi di tabel 'struk' terlebih dahulu
        if tabel == "pegawai":
            cursor.execute("DELETE FROM struk WHERE nama_pegawai = %s", (id_field,))
            conn.commit()
            
        elif tabel == "transaksi":
            cursor.execute("DELETE FROM struk WHERE no_transaksi = %s", (id_field,))
            conn.commit()

        # Jika tabel adalah 'produk', hapus dependensi di tabel 'struk' terlebih dahulu
        elif tabel == "produk":
            cursor.execute("DELETE FROM struk WHERE nama_produk = %s", (id_field,))
            conn.commit()

        # Hapus data di tabel utama
        cursor.execute(f"DELETE FROM {tabel} WHERE {primary_key}=%s", (id_field,))
        conn.commit()
        print(f"Data dari tabel {tabel} berhasil dihapus.")
    else:
        print("Pilihan tidak valid.")


def connect_database():
    return mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="penjualan"
    )

def main():
    conn = connect_database()
    cursor = conn.cursor()

    while True:
        menu = main_menu()

        if menu == 1:
            tambah_data(cursor, conn)
        elif menu == 2:
            tampilkan_data(cursor)
        elif menu == 3:
            ubah_data(cursor, conn)
        elif menu == 4:
            hapus_data(cursor, conn)
        elif menu == 5:
            print("Terima kasih telah menggunakan sistem manajemen penjualan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
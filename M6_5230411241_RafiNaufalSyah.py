class Order:
    def __init__(self, id: int, nama_barang: str, details: str):
        self._id = id
        self.nama_barang = nama_barang
        self.details = details  
    
    def setOrder(self, id: int, nama_barang: str, details: str):
        self._id = id
        self.nama_barang = nama_barang
        self.details = details
        
    def getOrder(self):
        return {
            "id": self._id,
            "nama_barang": self.nama_barang,
            "details": self.details
        }
    
class Delivery:
    def __init__(self, id: int, nama: str, informasi: str, tanggal: str, address: str):
        self._id = id
        self.nama = nama
        self.informasi = informasi
        self.tanggal = tanggal
        self.address = address
        
    def processDelivery(self):
        return f"Memproses delivery untuk {self.nama} ke {self.address} pada tanggal {self.tanggal}"
    
    def getDelivery(self):
        return {
            "id": self._id,
            "nama": self.nama,
            "informasi": self.informasi,
            "tanggal": self.tanggal,
            "address": self.address
        }

orders = []
deliveries = []

while True:
    print("\n====MENU====")
    print("1. Order")
    print("2. Delivery")
    print("3. Exit")
    print("============")
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        while True:
            print("\n====ORDER MENU====")
            print("1. Tambah Order")
            print("2. Lihat Order")
            print("3. Hapus Order")
            print("4. Kembali")
            print("==================")
            sub_pilihan = input("Pilih menu: ")
            
            if sub_pilihan == "1":
                id = int(input("Masukkan ID barang: "))
                nama_barang = input("Masukkan nama barang: ")
                details = input("Masukkan detail barang: ")
                order = Order(id, nama_barang, details)
                orders.append(order)
                print("Order berhasil ditambahkan.")
                
            elif sub_pilihan == "2":
                if orders:
                    print("List Order:")
                    for order in orders:
                        print(order.getOrder())
                else:
                    print("Tidak ada order.")
                    
            elif sub_pilihan == "3":
                id = int(input("Masukkan ID order yang akan dihapus: "))
                orders = [order for order in orders if order._id != id]
                print("Order berhasil dihapus.")
                
            elif sub_pilihan == "4":
                break
                
            else:
                print("Pilihan tidak valid, silakan coba lagi!")
                
    elif pilihan == "2":
        while True:
            print("\n====DELIVERY MENU====")
            print("1. Tambah Delivery")
            print("2. Lihat Delivery")
            print("3. Hapus Delivery")
            print("4. Kembali")
            print("=====================")
            sub_pilihan = input("Pilih menu: ")
            
            if sub_pilihan == "1":
                id = int(input("Masukkan ID delivery: "))
                nama = input("Masukkan nama penerima: ")
                informasi = input("Masukkan informasi delivery: ")
                tanggal = input("Masukkan tanggal delivery: ")
                address = input("Masukkan alamat delivery: ")
                delivery = Delivery(id, nama, informasi, tanggal, address)
                deliveries.append(delivery)
                print("Delivery berhasil ditambahkan.")
                
            elif sub_pilihan == "2":
                if deliveries:
                    print("List Delivery:")
                    for delivery in deliveries:
                        print(delivery.getDelivery())
                else:
                    print("Tidak ada delivery.")
                    
            elif sub_pilihan == "3":
                id = int(input("Masukkan ID delivery yang akan dihapus: "))
                deliveries = [delivery for delivery in deliveries if delivery._id != id]
                print("Delivery berhasil dihapus.")
                
            elif sub_pilihan == "4":
                break
                
            else:
                print("Pilihan tidak valid, silakan coba lagi!")
                
    elif pilihan == "3":
        print("Keluar program. . . . .")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi!")

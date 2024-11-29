import tkinter as tk
from tkinter import ttk, messagebox

# Simpan data hafalan dalam list
data_hafalan = []

# GUI Utama
class QuranApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Setor Hafalan Quran")
        self.root.geometry("700x500")
        
        # Frame Input
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)
        
        tk.Label(self.frame_input, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nama = tk.Entry(self.frame_input)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_input, text="Surat:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_surat = tk.Entry(self.frame_input)
        self.entry_surat.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_input, text="Ayat:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_ayat = tk.Entry(self.frame_input)
        self.entry_ayat.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_input, text="Status:").grid(row=3, column=0, padx=5, pady=5)
        self.combobox_status = ttk.Combobox(self.frame_input, values=["Lulus", "Belum Lulus"], state="readonly")
        self.combobox_status.grid(row=3, column=1, padx=5, pady=5)
        self.combobox_status.current(0)
        
        tk.Button(self.frame_input, text="Tambah", command=self.tambah_data).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Frame Pencarian dan Hapus
        self.frame_cari_hapus = tk.Frame(self.root)
        self.frame_cari_hapus.pack(pady=10)
        
        tk.Label(self.frame_cari_hapus, text="Cari Nama:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cari_hapus = tk.Entry(self.frame_cari_hapus)
        self.entry_cari_hapus.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(self.frame_cari_hapus, text="Cari Data", command=self.cari_data).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.frame_cari_hapus, text="Hapus Data", command=self.hapus_data).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(self.frame_cari_hapus, text="Refresh", command=self.refresh_data).grid(row=0, column=4, padx=5, pady=5)
        
        # Tabel
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nama", "Surat", "Ayat", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Surat", text="Surat")
        self.tree.heading("Ayat", text="Ayat")
        self.tree.heading("Status", text="Status")
        self.tree.column("ID", width=30)
        self.tree.pack(pady=10)
        
        self.load_data()
    
    # Tambah data ke list dan refresh tabel
    def tambah_data(self):
        nama = self.entry_nama.get()
        surat = self.entry_surat.get()
        ayat = self.entry_ayat.get()
        status = self.combobox_status.get()
        
        if nama and surat and ayat:
            # Tambahkan data ke dalam list
            new_data = {
                "id": len(data_hafalan) + 1,
                "nama_penyetor": nama,
                "surat": surat,
                "ayat": ayat,
                "status": status
            }
            data_hafalan.append(new_data)
            self.load_data()
            messagebox.showinfo("Berhasil", "Data berhasil ditambahkan!")
            
            # Kosongkan input
            self.entry_nama.delete(0, tk.END)
            self.entry_surat.delete(0, tk.END)
            self.entry_ayat.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Semua kolom harus diisi!")
    
    # Muat data dari list ke tabel
    def load_data(self, filtered_data=None):
        """Memuat data ke tabel, bisa seluruh data atau data yang disaring.""" 
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        data_to_display = filtered_data if filtered_data else data_hafalan
        for data in data_to_display:
            self.tree.insert("", tk.END, values=(data["id"], data["nama_penyetor"], data["surat"], data["ayat"], data["status"]))
    
    # Cari data berdasarkan nama
    def cari_data(self):
        nama_cari = self.entry_cari_hapus.get()
        if not nama_cari:
            messagebox.showerror("Error", "Masukkan nama yang ingin dicari!")
            return
        
        # Filter data berdasarkan nama
        filtered_data = [data for data in data_hafalan if nama_cari.lower() in data["nama_penyetor"].lower()]
        if filtered_data:
            self.load_data(filtered_data)
        else:
            self.load_data()
            messagebox.showinfo("Hasil Pencarian", f"Tidak ditemukan data dengan nama '{nama_cari}'!")
    
    # Hapus data berdasarkan nama
    def hapus_data(self):
        nama_hapus = self.entry_cari_hapus.get()
        if not nama_hapus:
            messagebox.showerror("Error", "Masukkan nama yang ingin dihapus!")
            return
        
        # Hapus data berdasarkan nama
        global data_hafalan
        data_hafalan = [data for data in data_hafalan if nama_hapus.lower() not in data["nama_penyetor"].lower()]
        
        # Perbarui ID setelah data dihapus
        for idx, data in enumerate(data_hafalan):
            data["id"] = idx + 1
        
        self.load_data()
        messagebox.showinfo("Berhasil", f"Semua data dengan nama '{nama_hapus}' berhasil dihapus!")
        self.entry_cari_hapus.delete(0, tk.END)
    
    # Refresh data untuk menampilkan semua data
    def refresh_data(self):
        self.load_data()
        self.entry_cari_hapus.delete(0, tk.END)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = QuranApp(root)
    root.mainloop()

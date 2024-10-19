class Music:
    def __init__(self, judul, artist, genre):
        self.judul = judul
        self.artist = artist
        self.genre = genre

    def display(self):
        return f"judul: {self.judul}, Artist: {self.artist}, Genre: {self.genre}"


class RockMusic(Music):
    def __init__(self, judul, artist):
        super().__init__(judul, artist, genre='Rock')


class PopMusic(Music):
    def __init__(self, judul, artist):
        super().__init__(judul, artist, genre='Pop')


class PunkMusic(Music):
    def __init__(self, judul, artist):
        super().__init__(judul, artist, genre='Jazz')


class ListMusic:
    def __init__(self):
        self.music_list = []

    def add_music(self, music):
        self.music_list.append(music)

    def delete_music(self, judul):
        self.music_list = [music for music in self.music_list if music.judul != judul]

    def display_all_music(self):
        sorted_music = sorted(self.music_list, key=lambda x: x.judul)
        for music in sorted_music:
            print(music.display())

    def search_by_artist(self, artist):
        found_music = [music for music in self.music_list if music.artist.lower() == artist.lower()]
        for music in found_music:
            print(music.display())


def main():
    list = ListMusic()

    list.add_music(RockMusic("Sekuat Hatimu", "Last Child"))
    list.add_music(RockMusic("Duka", "Last Child"))
    list.add_music(RockMusic("Arjuna", "Dewa 19"))
    list.add_music(RockMusic("Selamat jalan", "Tipe x"))
    list.add_music(RockMusic("Seandainya", "Vierra"))
    list.add_music(PopMusic("Halu", "Febi Putri"))
    list.add_music(PopMusic("Dan", "Sheila on 7"))
    list.add_music(PopMusic("Risalah hati", "Dewa 19"))
    list.add_music(PopMusic("Sial", "Mahalini"))
    list.add_music(PopMusic("Resah jadi luka", "Daun Jatuh"))
    list.add_music(PunkMusic("Hilang Harapan", "SHA"))
    list.add_music(PunkMusic("Sampai Nanti", "Threesixty Skatepunk"))
    list.add_music(PunkMusic("Dewi", "Threesixty Skatepunk"))
    list.add_music(PunkMusic("Sebuah Rahasia", "Pee Wee Gaskins"))
    list.add_music(PunkMusic("Terlatih Patah Hati", "The"))
    
    while True:
        print("\n============ PLAY MUSIC ============")
        print("1. Tampilkan Semua List Musik")
        print("2. Cari Musik Berdasarkan Penyanyi")
        print("3. Tambah Musik")
        print("4. Hapus Musik")
        print("5. Keluar")
        print("=====================================")
        choice = input("Masukkan Pilihan: ")

        if choice == '1':
            print("\nDaftar Musik:")
            list.display_all_music()
        elif choice == '2':
            artist = input("Masukkan nama penyanyi: ")
            print("\nHasil Pencarian:")
            list.search_by_artist(artist)
        elif choice == '3':
            judul = input("Masukkan judul musik: ")
            artist = input("Masukkan nama penyanyi: ")
            genre = input("Masukkan genre musik (Rock/Pop/Punk): ")
            if genre.lower() == 'rock':
                list.add_music(RockMusic(judul, artist))
            elif genre.lower() == 'pop':
                list.add_music(PopMusic(judul, artist))
            elif genre.lower() == 'Punk':
                list.add_music(PunkMusic(judul, artist))
            else:
                print("Genre tidak valid.")
        elif choice == '4':
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            list.delete_music(judul)
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
    
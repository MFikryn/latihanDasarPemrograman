def show_menu():
    print("\nMenu:")
    print("1. List Produk")
    print("2. Tambah Produk")
    print("3. Hapus Produk Berdasarkan Nama")
    print("4. Hapus Produk Berdasarkan No Produk")
    print("5. Keluar")

def list_produk(produk):
    if not produk:
        print("Daftar produk kosong.")
    else:
        for idx, p in enumerate(produk, 1):
            print(f"{idx}. {p}")

def tambah_produk(produk):
    nama_produk = input("Masukkan nama produk: ")
    produk.append(nama_produk)
    print(f"Produk '{nama_produk}' telah ditambahkan.")

def hapus_produk_nama(produk):
    nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
    if nama_produk in produk:
        produk.remove(nama_produk)
        print(f"Produk '{nama_produk}' telah dihapus.")
    else:
        print(f"Produk '{nama_produk}' tidak ditemukan.")

def hapus_produk_nomor(produk):
    try:
        nomor = int(input("Masukkan nomor produk yang ingin dihapus: "))
        if 1 <= nomor <= len(produk):
            removed_product = produk.pop(nomor - 1)
            print(f"Produk '{removed_product}' telah dihapus.")
        else:
            print("Nomor produk tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

def main():
    produk = []
    while True:
        show_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            list_produk(produk)
        elif pilihan == '2':
            tambah_produk(produk)
        elif pilihan == '3':
            hapus_produk_nama(produk)
        elif pilihan == '4':
            hapus_produk_nomor(produk)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()

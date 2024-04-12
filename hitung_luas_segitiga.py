def menu():
    print("Menu:")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil dan genap")
    print("4. Quit")
    choice = input("Pilih opsi: ")
    return choice

def hitung_luas_segitiga():
    try:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
    
        luas = 0.5 * alas * tinggi
        
        # Menampilkan hasil perhitungan
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah: {luas}")
    except ValueError:
        print("Input tidak valid. Pastikan alas dan tinggi adalah angka.")

def hitung_luas_persegi_panjang():
    try:
        # Meminta input panjang dan lebar persegi panjang dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        
        # Menghitung luas persegi panjang menggunakan rumus panjang * lebar
        luas = panjang * lebar
        
        # Menampilkan hasil perhitungan
        print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah: {luas}")
    except ValueError:
        print("Input tidak valid. Pastikan panjang dan lebar adalah angka.")

def tentukan_ganjil_genap():
    try:
        # Meminta input angka dari pengguna
        angka = int(input("Masukkan angka: "))
        
        # Menentukan apakah angka ganjil atau genap
        if angka % 2 == 0:
            print(f"Angka {angka} adalah angka genap.")
        else:
            print(f"Angka {angka} adalah angka ganjil.")
    except ValueError:
        print("Input tidak valid. Pastikan angka adalah bilangan bulat.")

def main():
    while True:
        choice = menu()
        
        if choice == '1':
            hitung_luas_segitiga()
        elif choice == '2':
            hitung_luas_persegi_panjang()
        elif choice == '3':
            tentukan_ganjil_genap()
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main ()

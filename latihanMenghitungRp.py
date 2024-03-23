def format_rupiah(amount):
    """Format angka menjadi format uang Rupiah."""
    return "Rp {:,}".format(amount).replace(",", ".")
def main():
    harga_supplier = int(input("Silakan Masukkan harga dari supplier (Rp): "))
    persen_keuntungan = int(input("Silakan masukkan persentase keuntungan yang Anda inginkan: "))
    harga_jual = harga_supplier * (1 + persen_keuntungan / 100)
    keuntungan = harga_jual - harga_supplier
    print("Harga dari supplier : ", format_rupiah(harga_supplier))
    print("Persen keuntungan: ", persen_keuntungan, "%")
    print("Keuntungan dari persen: ", format_rupiah(keuntungan))
    print("Harga jual: ", format_rupiah(harga_jual))

if __name__ == "__main__":
    main()
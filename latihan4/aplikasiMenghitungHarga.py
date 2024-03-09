# aplikasi menghitung harga jual berdasarkan persen
hargaSupplier = int(input("Silahkan Masukan harga dari supplier: "))
persen = int (input("silahkan persen keuntungan yang anda inginkan: "))
hargaPersen = hargaSupplier * (persen /100)
hargaJual = hargaSupplier + hargaPersen

print("Harga dari supplier : ",hargaSupplier)
print("persen keuntungan: ",persen)
print("keuntungan dari persen: ",hargaPersen)
print("Harga jual: ",hargaJual)
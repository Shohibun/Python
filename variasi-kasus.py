def daftar_menu(data1, data2, data3, harga_total, harga_varian, harga_topping, harga_ukuran):
    print("Selamat datang di toko Chatime afin, mau pesan varian apa ? ",
          "\n[1] Coklat",
          "\n[2] Matcha",
          "\n[3] Taro",
          "\n[4] Brownsugar",
          "\n[5] Caramel")
    pembeli = int(input("Masukkan angka untuk memilih varian rasa: "))
    
    for i in range(0, len(data1), 1):
        if pembeli == data1[i][0]:
            harga_varian += data1[i][2]
            print("Pilih topping yang diinginkan: ",
                  "\n[1] bubble",
                  "\n[2] Jelly",
                  "\n[3] Mangga slush")
            topping = int(input("Masukkan angka untuk memilih varian topping: "))
            for j in range(0, len(data2), 1):
                if topping == data2[j][0]:
                    harga_topping += data2[j][2]
                    print("Pilih ukuran yang diinginkan: ",
                          "\n[1] Reguler",
                          "\n[2] Large")
                    ukuran = int(input("Masukkan angka untuk memilih varian ukuran: "))
                    for x in range(0, len(data3), 1):
                        if ukuran == data3[x][0]:
                            harga_ukuran += data3[x][2]
                            harga_total = harga_varian + harga_topping + harga_ukuran
    if pembeli == 0:
        print("Pilihan tidak ada di daftar menu")
    
    print("Harga total : {}".format(harga_total))
    
data1 = [
    [1, "Coklat", 24000],
    [2, "Matcha", 26000],
    [3, "Taro", 21000],
    [4, "Brownsugar", 23000],
    [5, "Caramel", 22000]
]
data2 = [
    [1, "Bubble", 4000],
    [2, "jelly", 3000],
    [3, "Manngga Slush", 5000]
]
data3 = [
    [1, "Reguler", 3000],
    [2, "Large", 5000]
]

daftar_menu(data1, data2, data3, 0, 0, 0, 0)

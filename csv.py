import csv

nim = []
nama = []

def menu():
    print("Daftar Fitur: ")
    print("[1] Menampilakan isi data")
    print("[2] Menambahkan data")
    print("[3] Mencari data")
    print("[4] Menghapus data")
    print("[5] Mengurutkan data")
    print("[6] Searching data")
    print("[7] Exit", "\n")

    pilih = input("Masukkan pilihan: ")
    if pilih.lower() == "1":
        isi_data()
    elif pilih.lower() == "2":
        menambahkan_data()
    elif pilih.lower() == "3":
        mencari_data()
    elif pilih.lower() == "4":
        menghapus_data()
    elif pilih.lower() == "5":
        mengurutkan_data()
    elif pilih.lower() == "6":
        searching_data()
    elif pilih.lower() == "7":
        exit()
    else:
        print("Tidak ada di menu")
        back_to_menu()
#with open ini unutuk menampilan csv nya. saya gak makek disetiap def soalnya biar tidak error. 
with open ("DaftarNama.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        #row disini berarti dia itu menambahkan dari row indeks 0 dan indeks 1
        nim.append(row[0])
        nama.append(row[1])

#banc to menu disini untuk mengembalikan proses ke semula 
def back_to_menu():
    menu()

#fungsi ini untuk emnampilan csv dalam kesluruhan data. 
def isi_data():
    for isi in range (len(nim)):
        #print nim dan nama disni kenapa harus ada isi biar tahu itu akan di proses sebanyak len nim
        print(nim[isi], nama[isi])
    back_to_menu()

#fungsi untuk menambahkan data
def menambahkan_data():
    #Disini sudah terlihat kalau kita harus menginputkan terlebih dahulu baru bisa ditambahkan ke data
    nim_baru = input("Masukkan nim baru: ")
    nama_baru = input("Masukkan nama baru: ")
    nim.append(nim_baru)
    nama.append(nama_baru)
    back_to_menu()

#Fungsi untuk mencari suatu data
def mencari_data():
    pencari = input("Masukkan nama atau nim yang ingin dicari: ")
    #Ini saya memakai in biar pencari tuh bisa masuk dalam nim, soalnya kalau dijadikan perbandingan nanti error. 
    if pencari in nim:
        isi = nim.index(pencari)
        print(pencari, nama[isi])
    elif pencari in nama:
        isi = nama.index(pencari)
        print(nim[isi], nama)
    else: 
        print("Data yang anda cari tidak ditemukan")
    back_to_menu()

#Fungsi untuk menghapus data
def menghapus_data():
    penghapus = input("Masukkan nama atau nim yang ingin anda hapus: ")
    #Disini sudah terlihat bahwa memakai fungsi pop untuk menghapus sebuah data
    if penghapus in nim:
        isi = nim.index(penghapus)
        nim.pop(isi)
        nama.pop(isi)
        print("Pengahapusan berhasil dilakukan")
    elif penghapus in nama:
        isi = nama.index(penghapus)
        nim.pop(isi)
        nama.pop(isi)
        print("Pengahapusan berhasil dilakukan")
    back_to_menu()

def mengurutkan_data():
    #Disini saya dalam mengurutkan data memakai logika bubble sort. kalau descending tuh tinggal dibalik tanda > menjadi < 
    user = input("Masukkan kata nama ata nim untuk mengurutkan: ")
    if user.lower() == "nim":
        inputan = input("Masukkan kata ascending atau descending untuk menurutkan sesuai nilai: ")
        if inputan.lower() == "ascending":
            for i in range (len(nim)-1, 0, -1):
                for j in range (i):
                    if (int(nim[j])) > (int(nim[j+1])):
                        hmm = nim[j]
                        nim[j] = nim[j+1]
                        nim[j+1] = hmm
            for isi in range (len(nim)):
                print(nim[isi], nama[isi])
        elif inputan.lower() == "descending":
            for i in range (len(nim)-1, 0, -1):
                for j in range(i):
                    if (int(nim[j])) < (int(nim[j+1])):
                        hmm = nim[j]
                        nim[j] = nim[j+1]
                        nim[j+1] = hmm
            for isi in range (len(nim)):
                print(nim[isi], nama[isi])
    elif user.lower() == "nama":
        #Ini kenapa prosesnya bisa samapi panjang soalnya nim sama nama sama2 diproses biar nimnya ikut dengan namanya. 
        inputan = input("Masukkan kata ascending atau descending untuk menurutkan sesuai nilai: ")
        if inputan.lower() == "ascending":
            for i in range (len(nama)-1, 0, -1):
                for i in range (i):
                    if nama[i] > nama[i+1]:
                        hmm = nama[i]
                        nama[i] = nama[i+1]
                        nama[i+1] = hmm
                        hmm2 = nim[i]
                        nim[i] = nim[i+1]
                        nim[i+1] = hmm2
            for isi in range (len(nama)):
                print(nim[isi], nama[isi])
        elif inputan.lower() == "descending":
            for h in range (len(nama)-1, 0, -1):
                for i in range (h):
                    if nama[i] < nama[i+1]:
                        hmm = nama[i]
                        nama[i] = nama[i+1]
                        nama[i+1] = hmm
                        hmm2 = nim[i]
                        nim[i] = nim[i+1]
                        nim[i+1] = hmm2
            for isi in range (len(nama)):
                print(nim[isi], nama[isi])
    back_to_menu()

def searching_data():
    #Disini saya memakai binary search
    #ini jika saya mengurutkan terlebih dahulu malah tidak bisa mas
    #kalau langsung cari nim nya bisa 
    aku = input("Masukkan kata nama atau nim untuk mencari suatu data: ")
    if aku.lower() == "nim":
        kiri = 0
        kanan = len(nim)-1
        cari = input("Masukkan nim yang ingin kalian cari: ")
        while kiri <= kanan:
            mid = kiri + (kanan - kiri) // 2
            if cari.lower() == nim[mid]:
                print("Data ditemukan pada indeks ke: ", mid, "Dengan keterangan: ", cari, nama[mid])
                break
            elif cari > nim[mid]:
                kiri = mid + 1
            else:
                kanan = mid - 1
    elif aku.lower() == "nama":
        #program ini hanya bisa memanggil nama yang tidak memiliki kesamaan dengan nama yang lain mas. jadi lek ada yang sama gak bisa.
        #Saya dah coba pakek cara yang saya tahu tapi gak bisa mas
        #Ada satu cara mas tapi itu pakek metode linear search jadi saya gak jadi pakek. saya tetep pakek ini meskipun hanya bisa satu nama. 
        x = []
        kiri = 0
        kanan = len(nama)-1
        cari = input("Masukkan nama yang ingin kalian cari: ")
        while kiri <= kanan:
            mid = kiri + (kanan - kiri) // 2
            if cari.lower() in nama[mid].lower():
                print("Data ditemukan pada indeks ke: ", mid, "Dengan keterangan: ", nim[mid], nama[mid])
                break
            elif cari > nama[mid]:
                kiri = mid + 1
            else: 
                kanan = mid - 1
    back_to_menu()

#disini saya melakukan fungsi penyimpanan data biar data yang saya ubah bisa kesimpan. 
def exit():
    with open ("DaftarNama.csv", mode = "w", newline = "") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for i in range(len(nim)):
            csv_writer.writerow([nim[i],nama[i],""])

if __name__ == "__main__":
    menu()

#Mas codingan di laptop saya bisa jalan tapi di laptop temen saya gak bisa mas. Tapi beneran mas codingan ini bisa jalan.
#Saya tahu konsep codingan ini dari Petani kode mas. 

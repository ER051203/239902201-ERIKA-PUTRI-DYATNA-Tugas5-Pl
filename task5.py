print ("---MEMBACA ANGKA HINGGA -1 DAN MENCETAK JUMLAH ANGKA---")

input_angka = input("Masukkan angka : ") #input program
angka = input_angka.split()     #untuk memisahkan angka yang dimasukan
total = 0       #inisiassi total

for angka in angka:         #memasukan rumus
        angka = int(angka)
        if angka == -1:
            break
        total += angka

print("Jumlah semua angka yang dimasukkan adalah:", total) #tampilan hasil profram
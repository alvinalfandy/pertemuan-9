my_list = [100, 200, 300, 400, 500]

# Menampilkan elemen ke 3 dari variable my_list yaitu 300
print("Elemen ke-3:", my_list[2]) 

# Menampilkan elemen ke 2 sampai ke 4 dari variable my_list yaitu 300 , 400
print("Elemen ke-2 sampai ke-4:", my_list[1:4])

# Menampilkan elemen Terakhir dari variable my_list yaitu 500
print("Elemen terakhir:", my_list[-1])

# Menampilkan variable my_list Elemen ke 4 Sebelum di ubah
print("SEBELUM ELEMEN KE 4 DI UBAH :", my_list[3])
# Mengubah nilai elemen ke 4 variable my_list menjadi 450
my_list[3] = 450
# Menampilkan variable my_list Elemen ke 4 SebSetelah di ubah
print("SETELAH ELEMEN KE 4 DI UBAH :", my_list[3])

# Menampilkan ELEMEN my_list SEBELUM DI UBAH
print("ELEMEN my_list SEBELUM DI UBAH : ", my_list)
# Menganti nilai ke empat sampai elemen terakhir  menjadi 450,550
my_list[3:] = [450, 550]
# Menampilkan ELEMEN my_list SETELAH DI UBAH
print("ELEMEN my_list SETELAH DI UBAH : ", my_list)

myListA = [1, 3, 10, 12, 2];
myListB = [2, 4, 1, 10, 12];

#Ambil 2 bagian pertama list A dan jadikan list B
print('myListA:', myListA);
print('myListB:', myListB);
myListB[0:2] = myListA[0:2];
print('myListB setelah 2 bagian pertama list A ditambahkan:', myListB);

print('myListB sebelum ditambahkan String:', myListB)
myListB.append('iniString');
print('myListB sesudah ditambahkan String:', myListB)

print('myListB sebelum ditambahkan 3 nilai:', myListB)
# Menambahkan tiga nilai ke list_B yaitu 600,700,800
myListB.extend([600, 700, 800])
print("Menambahkan tiga nilai ke list_B yaitu 600,700,800 :")
print('myListB sesudah ditambahkan 3 nilai:', myListB)

print('myListA:', myListA);
print('myListB:', myListB);
myListC = myListA + myListB;
print('myListC, hasil penambahan list A dengan list B:', myListC);
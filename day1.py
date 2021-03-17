# VARIABLE
# name = "Giovaldi" #string
# tanggal_lahir = 3 #integer
# married = False #boolean
# berat_badan = 60.5 #float

# PRINT FUNCTION
# print(name)
# print(type(name))
# print(type(tanggal_lahir))
# print(type(married))
# print(type(berat_badan))

# OPERASI MATEMATIKA 
# +,-,*,/,%,**,//(bagi dibulatkan kebawah)

# angka_1 = 10
# angka_2 = 5
# angka_3 = "10"
# angka_4 = "5"

# print("hasil jumlah =", (angka_1+angka_2)) #penambahan dua tipe integer 
# print("hasil kurang =", (angka_1-angka_2)) #pengurangan dua tipe integer 
# print("hasil kali =",(angka_1*angka_2)) #perkalian dua tipe integer 
# print("hasil bagi =",(angka_1/angka_2)) #pembagian dua tipe integer 
# # print(angka_1+angka_3) #akan menimbulkan error karena tidak dapat melakukan operasi penjumlahan antara dua tipe data berbeda
# # print(angka_1-angka_3) #akan menimbulkan error karena tidak dapat melakukan operasi pengurangan antara dua tipe data berbeda
# print("hasil jumlah ", angka_3+angka_4) #penambahan dua tipe string : 105 

# #memodifikasi string menjadi integer agar dapat melakukan pertambahan
# print("hasil jumlah int =",angka_1+int(angka_3))

# #memodifikasi integer menjadi string agar dapat melakukan pertambahan
# print("hasil jumlah str =",str(angka_1)+angka_3)

# #perkalian
# print("hasil kali =",angka_1*angka_3) #membuat string sebanyak 10x

# #pembagian
# print("hasil bagi =",angka_2/angka_1)

# #modulus / sisa bagi
# print("hasil modulus =",angka_2%angka_1)

# #pangkat
# print("hasil pangkat =",angka_2)

# INPUT FUNCTION
# a = input("masukan nama: ")
# print(type(a))

# SOAL 1 : OUTPUT yang diharapkan
## nama saya "input nama", umur saya "input umur", dan saya "input jenis kelamin"

# nama = input("masukkan nama:")
# umur = int(input("umur saya:"))
# jenis_kelamin = input("masukkan jenis kelamin:")

#cara 1
# print("\ncara1")
# print("Nama saya",nama,"umur saya",umur,"tahun, dan saya",jenis_kelamin)

# #cara 2
# print("\ncara2")
# print("Nama saya {}, umur saya {} tahun, dan saya adalah {}".format(nama,umur,jenis_kelamin))

# #cara 3
# print("\ncara3")
# print(f"Nama saya {nama},umur saya {umur} tahun, dan saya adalah {jenis_kelamin}")

# name : Lingard
# age : 22 years old
# sex : men
# position : LMF
# overall : 67

# name = input("masukkan nama pemain:")
# age = int(input("masukkan umur:"))
# sex = input("masukkan jenis kelamin:")
# position = input("masukkan posisi pemain:")
# overall = int(input("masukkan overall:"))
# print("Nama saya", name, "umur saya", age, "jenis kelamin saya",sex,"posisi saya",position,"overall",overall)

#FUNCTION MATH 
#ceil (bulatkan ke atas), pow (pangkat), floor(bulatkan kebawah), sqrt (akar)
# import math

# x = 5.7

# print(math.ceil(x)) 
# print(math.pow(x,2))
# print(math.floor(x))
# print(math.sqrt(x))
# print(round(x))

#STRINGS
# nama = "marion jola"
# hitung jumlah karakter
# print(len(nama))
# # lower case untuk string
# print(nama.lower())
# # upper case untuk string
# print(nama.upper())
# # capitalize (huruf depannya aja yang besar)
# print(nama.capitalize())
# # title (huruf depan tiap kata dibesarkan)
# print(nama.title())

# # SPLIT FUNCTION
# print(nama.split())
# print(nama.split("a"))

# # string indexing
# print(nama[8:])
# print(nama[7])
# print(nama[1:10])
# print(nama[:15])

# string quotes
# singlequotes ='single quotes'
# doublequotes ="double quotes"
# combinequotes =" i don't know"

# a, b = 6,5
# a, b = b,a
# print(a)
# print(b)

#Intro to Python

# SOAL 1
x =4
y =3
z =2

w = ((x+y*z)/(x*y))**z
print(w) 

# CARA2
import math
x = 4
y = 3
z = 2
w = (math.pow((x + y * z)/(x*y),z))

print(w)

# SOAL 2
angka = int(input("Silahkan masukkan angka berapapun :"))
kuadrat = angka**2
print("Kuadrat dari",angka,"=",kuadrat)


# CARA2
#fungsi int(input()) digunakan untuk membuat input dengan tipe data integer/angka
#fungsi kuadrat menggunakan math.pow
angka = int(input("Masukkan Angka : "))
kuadrat = math.pow(angka,2)

print("Kuadrat dari {} adalah {}".format(angka,kuadrat))

# SOAL 3
import math
n = int(input("masukkan hari:"))
tahun = 360
bulan = 30
minggu = 7
hari = 1

tahun_ = math.floor(n/tahun)
# print(tahun_)
bulan_ = math.floor((n%tahun)/bulan)
# print(bulan_)
minggu_ = math.floor((tahun%bulan)/minggu)
# print(minggu_)
hari_ = math.floor(n%bulan%minggu)
# print(hari_)

print(n,"hari =",tahun_,"tahun ,",bulan_,"bulan ,",minggu_,"minggu ,",hari_,"hari")

# SOAL 4
total_ab = 49
rasio = 0.4
Budi = total_ab/1.4
Andi = total_ab - Budi
UsiaAndi = Andi + 2
UsiaBudi = Budi + 2

print(" Usia Andi dan Budi 2 tahun lagi adalah {} dan {}".format(UsiaAndi,UsiaBudi))

# SOAL 5
Masukan = "purwadhika"
Huruf = input("Masukan Huruf : ")
Jumlah = Masukan.count(Huruf)

print("Jumlah huruf {} pada {} adalah {}".format(Huruf,Masukan,Jumlah))

# SOAL 6 rumus = t : s/v
S_ab = 120
V_a = 60
V_b = 40
TAwal = 9
Menit = 60
T_ab = (S_ab /(V_a +V_b)) * Menit
TJam = math.floor(T_ab/Menit)
MenitTabrak = T_ab % Menit
JamTabrak = TAwal + TJam 

print("A dan B akan tertabrak pada jam {} lewat {} menit".format(JamTabrak,MenitTabrak))








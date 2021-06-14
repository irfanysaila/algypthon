TRANSAKSI PEMBELIAN PRINTER EPSON T20.py
@@ -0,0 +1,16 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:05:38 2021
@author: My Device is Awesome
"""
hargaprint = 660000

print ("TRANSAKSI PEMBELIAN PRINTER EPSON T20")
print ("=====================================")

JmlBeli = input ("Jumlah printer epson T20 yang dibeli = ")

total = int(hargaprint)*int(JmlBeli)

print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (total))
 26  cek golongan usia.py 
@@ -0,0 +1,26 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:49:58 2021
@author: My Device is Awesome
"""

print(" CEK GOLONGAN USIA ")
print ("=========================")

u = input("Masukkan Usia = ")

if int(u)>0 and int(u)<=100:
    if int(u)>=60: 
        sts="lansia"
    elif int(u)>=35: 
        sts="dewasa"
    elif int(u)>=18: 
        sts="pemuda"
    elif int(u)>=15: sts="remaja"
    else:
        sts="anak"
    print (sts)
else:
    pesan="Masukkan angka usia 0-100 saja"
    print(pesan) 
 24  cek kelulusan.py 
@@ -0,0 +1,24 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:55:54 2021
@author: My Device is Awesome
"""

jwb = "y"
while jwb=="y" or jwb=="Y":

    print ("=========================")
    print(" CEK KELULUSAN ")
    print ("=========================")

    n = input(">> Masukkan Nilai = ")

    if int(n)>60:
        sts = "LULUS"
    else:
        sts="ULANG"
    print(sts)
jwb = input("Mulai lagi?")
    if jwb== "t":
        break 
 28  cek nilai.py 
@@ -0,0 +1,28 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:57:24 2021
@author: My Device is Awesome
"""

print("Cek Nilai")
print ("=========================")

n = input("Masukkan Nilai = ")

if int(n)>0 and int(n)<=100:
    if int(n)>80: 
        sts="Baik Sekali"
    elif int(n)>=65: 
        sts="Baik"
    elif int(n)>=55: 
        sts="Cukup"
    elif int(u)>=40:
        sts="Kurang"

    else:
        sts="Kurang Sekali"
    print (sts)
else:
    pesan="Masukkan angka 0-100 saja"
    print(pesan) 
 25  penilaian mahasiswa.py 
@@ -0,0 +1,25 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:01:34 2021
@author: My Device is Awesome
"""

print("Penilaian Mahasiswa")
print ("=========================")

n = input("Masukkan Nilai = ")

if int(n)>0 and int(n)<=100:
    if int(n)>=91 and int(n)<100: 
        sts="A"
    elif int(n)>=81 and int(n)<91: 
        sts="B"
    elif int(n)>=71 and int(n)<81: 
        sts="C"
    elif int(n)<71:
        sts="D"

else:
    pesan="Masukkan angka 0-100 saja"
    print(pesan) # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


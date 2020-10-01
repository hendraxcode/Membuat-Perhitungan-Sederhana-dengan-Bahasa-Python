def penjumlahan (a,b):
    penjumlahan = a+b
    return penjumlahan
def pengurangan (a,b):
    pengurangan = a-b
    return pengurangan
def perkalian(a,b):
    perkalian = a*b
    return perkalian
def pembagian (a,b):
    pembagian = a/b
    return pembagian

lagi= 'y'
while lagi=='y':
    print ' \t \t Program Kalkulator Sayur'
    a= int(input(' Masukan Bilangan pertama : '))
    b= int(input(' Masukan Biilangan kedua : '))
    print ' 1. Penjumlahan \n 2. pengurangan \n 3. perkalian \n 4. pembagian \n'
    pilihan = input ('Pilih 1-5 : ')
    if pilihan == 1:
        print ' Hasilnya adalah = ', penjumlahan (a,b)
    elif pilihan == 2:
        print ' Hasilnya adalah = ', pengurangan (a,b)
    elif pilihan ==3 :
        print 'Hasilnya adalah = ', perkalian (a,b)
    elif pilihan ==4 :
        print 'Hasilnya adalah = ', pembagian (a,b)
    else :
        print 'masukan pilihan yang benar'

    lagi=raw_input(" Mau Lagi ?[y/t] : ")

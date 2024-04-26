import os

# menghitung keliling dan pergsegi panjang 
# os.system('cls')
# print(f'{'PROGRAM MENGHUTUNG LUAS':^40}')
# print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
# print(f'{'-'*40:^40}')

# lebar  = int(input('Masukan Nilai lebar : '))
# panjang  = int(input('Masukan Nilai panjang: '))

# luas = panjang * lebar
# keliling = 2*(panjang+lebar)

# print(f'hasil perhitungan luas {luas}')
# print(f'hasil perhitungan keliling {keliling}')

def header():
    os.system('cls')
    print(f'{'PROGRAM MENGHUTUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print(f'{'-'*40:^40}')
    
def inputUser():
    lebar  = int(input('Masukan Nilai lebar : '))
    panjang  = int(input('Masukan Nilai panjang: '))
    return lebar, panjang

def hitungLuas(lebar, panjang):
    luas = panjang * lebar
    return luas

def hitungKeliling(lebar, panjang):
    keliling = 2*(panjang+lebar)
    return keliling

while True:
    header()
    LEBAR, PANJANG = inputUser()
    LUAS = hitungLuas(LEBAR,PANJANG)
    PANJANG = hitungKeliling(LEBAR,PANJANG)
    
    print(f'hasil perhitungan luas {LUAS}')
    print(f'hasil perhitungan keliling {PANJANG}')
    isContinue = input('Apakah Ingin Lanjut (y/n)')
    if isContinue == 'n':
        break
print('Program Selesai')    
        
        
            
        
def sayHello(nama):
    "funsgi dengan default argument"
    print(f"Hallo {nama}")
    
def sayHello2(nama = 'maulana'):
    "funsgi dengan default argument"
    print(f"Hallo {nama}")
    
sayHello('maulana')
sayHello2()

def fungsiTambah(a,b):
    hasil = a + b
    return hasil
def fungsiKuadrat(inputKuadrat):
    outputKuadrat = inputKuadrat**2
    return outputKuadrat

print(fungsiTambah(1112,29))
print(fungsiKuadrat(4))

# bisa juga dengan return yang banyak 

def operasiMatematika(inputA, inputB):
    tambah = inputA + inputB
    kurang = inputA - inputB
    kali = inputA * inputB
    bagi = inputA / inputB
    return tambah, kurang, kali, bagi

nTambah,nKurang,nKali, nBagi = operasiMatematika(9,8)

print(f'Hasil Tambah = {nTambah}')
print(f'Hasil Kurang = {nKurang}')
print(f'Hasil Kali = {nKali}')
print(f'Hasil Bagi = {nBagi}')
print('Hello  World')

a = 10
b = 20

print(a  + b,  'hasil')

# variable sama kaya js (let) tanpa perlu deklarasi dan dapat di ubah nilainya

# type data sama dengan js tapi ada type data khusus dan kompleks

    # type data  biasa
typeInt = 10
typefloat = 10.5
typeStr = 'maulana'
typeBool = True 

    # type data khusus

dataComplex = complex(5, 6)
print('data: ', dataComplex)
print('Type: ', type(dataComplex))

    # bisa pake type data bahasa C
    
from ctypes import c_double
dataC_Double = c_double(10.5)

print('data: ', dataC_Double)
print('Type: ', type(dataC_Double))

# merubah data dari 1 type ke  tyope yang  lain casting

dataInt = 9
dataFloat = float(dataInt) # jika floatt ke integer akan di bulatkan ke bawah
dataStr = str(dataInt) # dari string ke integer bisa asalkan stringnya angka, jika  tidak error
dataBool = bool(dataInt) # akan false  jikanilai integer  = 0, jika string kosong jadi false
print('dataFloat: ', dataFloat)
print('dataStr: ', dataStr)
print('dataBool: ', dataBool)

letA = 10
letB = 20

print(letA == letB)
print(letA != letB)

#  format string 
nameTest = 'maulana'
formatSTR = f"Muhamad {nameTest}"
print(formatSTR)

#  waktu
import datetime as apaAjaBebas

hariIni = apaAjaBebas.date.today()

print(hariIni)
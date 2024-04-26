print('Hello  World')

a = 10
b = 20

    # print(a  + b,  'hasil')   

# variable sama kaya js (let) tanpa perlu deklarasi dan dapat di ubah nilainya

# type data sama dengan js tapi ada type data khusus dan kompleks

    # type data  biasa
typeInt = 10
typefloat = 10.5
typeStr = 'maulana'
typeBool = True 

    # type data khusus

dataComplex = complex(5, 6)
    # print('data: ', dataComplex)
    # print('Type: ', type(dataComplex))

    # bisa pake type data bahasa C
    
from ctypes import c_double
dataC_Double = c_double(10.5)

    # print('data: ', dataC_Double)
    # print('Type: ', type(dataC_Double))

# merubah data dari 1 type ke  tyope yang  lain casting

dataInt = 9
dataFloat = float(dataInt) # jika floatt ke integer akan di bulatkan ke bawah
dataStr = str(dataInt) # dari string ke integer bisa asalkan stringnya angka, jika  tidak error
dataBool = bool(dataInt) # akan false  jikanilai integer  = 0, jika string kosong jadi false
    # print('dataFloat: ', dataFloat)
    # print('dataStr: ', dataStr)
    # print('dataBool: ', dataBool)

letA = 10
letB = 20

    # print(letA == letB)
    # print(letA != letB)

#  format string 
nameTest = 'maulana'
formatSTR = f"Muhamad {nameTest}"
    # print(formatSTR)

#  waktu
import datetime as apaAjaBebas

hariIni = apaAjaBebas.date.today()

    # print(hariIni)

# tuples
dataTuples = (1,2,3,4,5) # data tuples tidak bisa  di ubah

# sets
dataSets = {23,34,345,5463,4562,452} # gak  punya index

# dictonary atau object klo  di js

dataDictonary = {
    "key1": 'value1',
    "key2": 'value2',
    "key3": 'value3',
}

key = 'key1'

CheckKey = key in dataDictonary  # mengecek key
# print(CheckKey)

# print(dataDictonary['key5'])
# print(dataDictonary.get('key5')) # pagai get,mendadakan dia  dictonary atau bukan dan jika tidak ada isinya akan none bukan err

#update data
dataDictonary.update({'key1': 'maulana'})
dataDictonary.update({'key4': 'maulana2'}) # jika key tidak terdaftar maka data akan di add/post
# print(dataDictonary)

#delete data
del dataDictonary['key1']
# print(dataDictonary)

# loopDictonary 

for datas in dataDictonary.keys():
    print(dataDictonary.get(datas)) # menggambil value dari data object/ dictonary dengankey dan value
    
for datas2  in dataDictonary.values():
    print(datas2, 'valuesss')   
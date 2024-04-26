# fungsi *args ( untuk menghandle data list) 
def fungsiArgs(*args):
    nama  = args[0]
    tinggi  = args[1]
    berat  = args[2]
    print(f'{nama} punya tinggi {tinggi}, dan berat {berat}')
    
fungsiArgs('maulana', 29, 45)

# fungsi **args ( untuk menghandle data list dengn key) 
def fungsiKeyArgs(**keyArgs):
    nama  = keyArgs['nama']
    tinggi  = keyArgs['tinggi']
    berat  = keyArgs['berat']
    print(f'{nama} punya tinggi {tinggi}, dan berat {berat}')
    
fungsiKeyArgs(nama='maulana',tinggi=29,berat=45)
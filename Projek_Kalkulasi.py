input = input("Masukkan kalimat: ")

number = []
tambah = False
kurang= False


for i in input:
    
    if(47 < ord(i) < 58):
        if(tambah):
            number.append(int(i))
        elif(kurang):
            number.append(int(i)*-1)
        else:
            number.append(int(i))

        tambah = False
        kurang = False
    
    else:
        if(i == '+'):
            tambah = True
        elif(i == '-'):
            kurang= True

print(sum(number))
import base64

def name_input_file():
    name_file=input("Введіть ім'я файла: ")
    with open('input.txt', 'r') as file:
        key="".join(file.readline().split())
        vec="".join(file.readline().split())
        text=file.read()
    return key, vec, text


def inisialisation_for_key(key):
    key_1=key[0:4]
    key_2=key[4:8]
    key_3=key[8:12]
    key_4=key[12:16]
    key_5=key[16:20]
    key_6=key[20:24]
    key_7=key[24:28]
    key_8=key[28:32]
    keys=[key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8]
    keys_revers=[""]*8
    for i in range(len(keys)):
        keys_revers[i]=keys[i][2:4]+keys[i][0:2]


    return keys_revers

def sdvic(arr, i):
    arr=bin((arr))[2:]
    arr= arr.zfill(32)
    arr=[int(x) for x in arr]
    for j in range(i):
        x=arr.pop(0)
        arr.append(x)
    
    arr=''.join(str(x) for x in arr)
    arr=(int(arr, 2))
    return arr

    
def Init(key, vec):
    schitaet=-9
    x=[0]*8
    c=[0]*8
    key=inisialisation_for_key(key)
    for j in range(8):
        if j%2==0:
            x[j]=key[(j+1)%8]+key[(j)%8]
            c[j]=key[(j+4)%8]+key[(j+5)%8]
        else:
            x[j]=key[(j+5)%8]+key[(j+4)%8]
            c[j]=key[j]+key[(j+1)%8]
    
    b=0
    for i in range(8):
        x[i]=int(x[i], 16)
        c[i]=int(c[i], 16)
       
    for i in range(4):
        schitaet+=1
        b, x, c=next(b, x, c)
    vec1=vec[0:8]
    vec1_reves=''
    l=len(vec1)-1
    for i in range(0, len(vec1), 2):
        vec1_reves+=vec1[l-i-1: l-i+1]
    vec1=int(vec1_reves, 16)
    vec2=vec[8:]
    vec1_reves=''
    l=len(vec2)-1
    for i in range(0, len(vec2), 2):
        vec1_reves+=vec2[l-i-1: l-i+1]
    vec2=int(vec1_reves, 16)
    c[0]=c[0]^x[4]^vec1
    
    c[2]=c[2]^x[6]^vec2
    c[4]=c[4]^x[0]^vec1
    c[6]=c[6]^x[2]^vec2
    
    vec1=vec[12:16]
    vec1_reves=''
    l=len(vec1)-1
    for i in range(0, len(vec1), 2):
        vec1_reves+=vec1[l-i-1: l-i+1]
    vec2=vec[4:8]
    vec2_reves=''
    l=len(vec2)-1
    for i in range(0, len(vec2), 2):
        vec2_reves+=vec2[l-i-1: l-i+1]
    vec2=vec1_reves+vec2_reves
    vec2=int(vec2, 16)
    c[1]=c[1]^x[5]^vec2
    c[5]=c[5]^x[1]^vec2
    
    vec1=vec[0:4]
    vec1_reves=''
    l=len(vec1)-1
    for i in range(0, len(vec1), 2):
        vec1_reves+=vec1[l-i-1: l-i+1]
    vec2=vec[8:12]
    vec2_reves=''
    l=len(vec2)-1
    for i in range(0, len(vec2), 2):
        vec2_reves+=vec2[l-i-1: l-i+1]
    vec1=vec2_reves+vec1_reves
    vec1=int(vec1, 16)
    c[3]=c[3]^x[7]^vec1
    c[7]=c[7]^x[3]^vec1
    schitaet+=1
    for i in range(4):
        schitaet+=1

        b, x, c=next(b, x, c)

    return b, x, c


    

def strm(a):
    x=a[:]
    x_1=[0]*8
    x_2=[0]*8
    
    for j in range(len(x)):
        x[j]=hex(x[j])[2:].zfill(8)
        for_x_1_1=x[j][6:8] 
        for_x_1_2=x[j][4:6]
        for_x_2_1=x[j][2:4]
        for_x_2_2=x[j][0:2]  

        x_1[j]=int(for_x_1_1+for_x_1_2, 16)  
        x_2[j]=int(for_x_2_1+for_x_2_2, 16)

    z_glavn=[0]*8
    z_glavn[0]=x_1[0] ^ x_2[5]
    z_glavn[1]=x_2[0] ^ x_1[3]
    z_glavn[2]=x_1[2] ^ x_2[7]
    z_glavn[3]=x_2[2] ^ x_1[5]
    z_glavn[4]=x_1[4] ^ x_2[1]
    z_glavn[5]=x_2[4] ^ x_1[7]
    z_glavn[6]=x_1[6] ^ x_2[3]
    z_glavn[7]=x_2[6] ^ x_1[1]

    return z_glavn


def delaem_udubno(temp):
    temp=hex(temp)
    arr=bin(int(temp, 16))[2:]
    arr=[int(x) for x in arr]
    x=0
    if len(arr)>32:
        x=arr.pop(0)
    arr=''.join(str(x) for x in arr)
    arr=int(arr, 2)
    return arr, x



def function_g(x, c):
    temp=(x+c)
    temp=(temp%(2**32))**2
    temp_1=temp& 0xFFFFFFFF
    temp_2=(temp>>32)&0xFFFFFFFF
    return temp_1^temp_2
    

def next(b, x, c):
    arr=[0x4d34d34d, 0xd34d34d3, 0x34d34d34, 0x4d34d34d, 0xd34d34d3, 0x34d34d34, 0x4d34d34d, 0xd34d34d3]
    b_arr=[0]*9
    b_arr[0]=b
    for j in range(8):
        temp=c[j]+arr[j]+b_arr[j]
        temp, b_arr[j+1]=delaem_udubno(temp)
        c[j]=temp
    b=b_arr[8]
    g=[0]*8
    mod=2**32
    for j in range(8):
        g[j]=function_g(x[j], c[j])
        h=str(hex(g[j]))[2:]
        g[j]=int(h, 16)
    

  
    for i in range(8):
        if i%2==0:
            t=((g[i]) + (sdvic(g[i-1], 16)))%mod
            x[i] = (t+sdvic(g[i-2], 16))%mod
        else:
            t=int(g[i]+sdvic(g[i-1], 8))%mod
            x[i]=(t+g[i-2])%mod

    return b, x, c
def chitaem_z(keys, vec, arr):
    b, x, c=Init(keys, vec)
    for i in range(4):
        b, x, c =next(b, x, c)
        z=strm(x)
        for i in range(len(z)):
             arr.append(z[i])
    return arr

def EncryptData(keys, vec,  text):
    text=text.encode("utf-8")
    z=[]
    z=chitaem_z(keys, vec, z)
    z_output=bytearray()
    for i in range(len(z)):
        z_output+=z[i].to_bytes(2, 'big')
    
    shifr=bytearray(len(text))
    for i in range(len(text)):
        shifr[i]=text[i]^z_output[i%len(z)]

    
    
    shifr=base64.b64encode(shifr).decode('utf-8')
    return shifr

def DecryptData(keys, vec,  text):
    text=base64.b64decode(text)
    z=[]
    z=chitaem_z(keys, vec, z)
    z_output=bytearray()
    for i in range(len(z)):
        z_output+=z[i].to_bytes(2, 'big')
    shifr=bytearray(len(text))
    for i in range(len(text)):
        shifr[i]=text[i]^z_output[i%len(z)]
    shifr=shifr.decode("utf-8")
    return shifr







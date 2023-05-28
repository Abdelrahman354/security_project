from tkinter import *
import pyDes

root = Tk()
root.geometry("800x600")
root.title("Cipher")

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
            return False

def Ceaser_encription ():       

    if (entryText.get()!="" or entryKey.get()!="") :
        alphArr ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text = entryText.get().upper()
        key = int(entryKey.get())
        temp1 = []
        z = 0
        abdo = ""
        for i in text:
            temp1.append(alphArr.index(text[z]))
            z += 1
        for i in temp1 :
            abdo+= alphArr[(i+key+26)%26]
        ceaserEncLb["text"] = "Result: "+abdo
    else:
        handlingLb["text"]="Please Enter Correct Inputs"
    

def Ceaser_decription():
    if entryText.get()!="" or entryKey.get()!="":
        alphArr ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_text=entryText.get().upper()
        key = int(entryKey.get())
        temp1=[]
        z=0
        abdo=""
        for i in cipher_text:
            temp1.append(alphArr.index(cipher_text[z]))
            z+=1
        for i in temp1 :
            abdo+=alphArr[(i-key+26)%26]
        ceaserDecLb["text"] = "Result: "+abdo
    else:
        handlingLb["text"]="Please Enter Correct Inputs"

def Vigenere_encription():
    if entryText.get()!="" or entryKey.get()!="":
        alphArr ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text=entryText.get().upper()
        key=entryKey.get().upper() 
        matrix = [[0 for x in range(26)] for y in range(26)]
        temp1=[]
        temp2=[]
        abdo=""
        z=0
        for i in range(26):
            for j in range(26):
                matrix[i][j] = alphArr[z%26]
                z+=1
            z+=1
        for i in text:
            temp1.append(alphArr.index(i))      
        for i in range(len(text)):       
            temp2.append(alphArr.index(key[i%len(key)]))        
        for i in range (len(text)):
            abdo+=matrix[temp1[i]][temp2[i]]
        vigenereEncLb["text"] = "Result: "+abdo
    else:
        handlingLb["text"]="Please Enter Correct Inputs"

def Vigenere_decription():
    if entryText.get()!="" or entryKey.get()!="":
        alphArr ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text=entryText.get().upper()
        key=entryKey.get().upper() 
        matrix = [[0 for x in range(26)] for y in range(26)]
        temp1=[]
        abdo=""
        x=0
        y=0
        for i in range(0,26):
            for j in range(0,26):
                matrix[i][j] = alphArr[x%26]
                x+=1
            x+=1
        for i in range(len(text)):
            temp1.append(alphArr.index(key[i%len(key)]))
        for i in text:
            for j in range(0,26) :
                if matrix[temp1[y]][j]==i:
                    abdo+=matrix[0][j]
            y+=1   
        vigenereDecLb["text"] = "Result: "+abdo
    else:
        handlingLb["text"]="Please Enter Correct Inputs"


def create_matrix(key):
    alphArr = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [["", "", "", "", ""],
              ["", "", "", "", ""],
              ["", "", "", "", ""],
              ["", "", "", "", ""],
              ["", "", "", "", ""]]
    p = ""
    m = 0
    for letter in key + alphArr:
        if letter not in p:
            p += letter
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = p[m]
            m += 1
    return matrix


def find_element(plaintext, matr):
    arr_index_element = []
    for pl in plaintext:
        for i in range(0, 5):
            for j in range(0, 5):
                if matr[i][j] == pl:
                    arr_index_element.append(i)
                    arr_index_element.append(j)
    return arr_index_element


def playfair_encription():
    if entryText.get()!="" or entryKey.get()!="":
        plaintext=entryText.get()
        key=entryKey.get()
        ciphertext = ''
        plaintext = plaintext.upper().replace('J', 'I').replace(' ', '').replace(' ', '')
        for i in range(len(plaintext) - 1):
            if plaintext[i] == plaintext[i+1] and i % 2 == 0:
                plaintext = plaintext[:i+1] + 'X' + plaintext[i+1:]
        if len(plaintext) % 2 == 1:
            plaintext += 'X'
        matr = create_matrix(key.upper().replace('J', 'I').replace(' ', ''))
        arr_index_element = find_element(plaintext, matr)
        for ind in range(0, len(arr_index_element), 4):
             if arr_index_element[ind+1]==arr_index_element[ind+3]:
                ciphertext+=matr[(arr_index_element[ind]+1) %5][arr_index_element[ind+1]]
                ciphertext+=matr[(arr_index_element[ind+2]+1 )%5][arr_index_element[ind+3]] 

             elif arr_index_element[ind]==arr_index_element[ind+2]:
                ciphertext+=matr[arr_index_element[ind]]  [(arr_index_element[ind+1]+1)%5]
                ciphertext+=matr[arr_index_element[ind+2]]  [(arr_index_element[ind+3]+1 ) %5]

             else:
                ciphertext+=matr[arr_index_element[ind]][arr_index_element[ind+3]]
                ciphertext+=matr[arr_index_element[ind+2]][arr_index_element[ind+1]]
        playFairEncLb["text"] = "Result: "+ciphertext
    else:
        handlingLb["text"]="Please Enter Correct Inputs"


def playfair_decription():
    if entryText.get()!="" or entryKey.get()!="":        
        chiphertext=entryText.get()
        key=entryKey.get()
        text = ''
        chiphertext = chiphertext.upper().replace('J', 'I').replace(' ', '')
        for i in range(len(chiphertext) - 1):
            if chiphertext[i] == chiphertext[i+1] and i % 2 == 0:
                chiphertext = chiphertext[:i+1] + 'X' + chiphertext[i+1:]
        if chiphertext[len(chiphertext)-1]=="x":
            chiphertext=chiphertext[0:len(chiphertext)-2]
        matr = create_matrix(key.upper().replace('J', 'I').replace(' ', ''))
        arr_index_element = find_element(chiphertext, matr)
        for ind in range(0, len(arr_index_element), 4):
             if arr_index_element[ind+1]==arr_index_element[ind+3]:
                text+=matr[(arr_index_element[ind]-1) %5][arr_index_element[ind+1]]
                text+=matr[(arr_index_element[ind+2]-1 )%5][arr_index_element[ind+3]] 

             elif arr_index_element[ind]==arr_index_element[ind+2]:
                text+=matr[arr_index_element[ind]]  [(arr_index_element[ind+1]-1)%5]
                text+=matr[arr_index_element[ind+2]]  [(arr_index_element[ind+3]-1 ) %5]

             else:
                text+=matr[arr_index_element[ind]][arr_index_element[ind+3]]
                text+=matr[arr_index_element[ind+2]][arr_index_element[ind+1]]
        playFairDecLb["text"] = "Result: "+text
    else:
        handlingLb["text"]="Please Enter Correct Inputs"


def Des_encription():
    if entryText.get()!="" or entryKey.get()!="":
        text = entryText.get()
        key = entryKey.get()
        des = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        abdo = des.encrypt(text).hex()
        print(abdo)
        desEncLb["text"] = "Result: "+str(abdo)
   
    else:
        handlingLb["text"]="Please Enter Correct Inputs"


def Des_decription():
    if entryText.get()!="" or entryKey.get()!="":
        text = bytes.fromhex(entryText.get())
        key = entryKey.get()
        des = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        abdo = des.decrypt(text)
        desDecLb["text"] = "Result: "+str(abdo)
    else:
        handlingLb["text"]="Please Enter Correct Inputs"


welcomeLb=Label(root,text="Hello, This is my Network Security Project",font="30",bg="black",fg="white")
handlingLb=Label(root,text="Thanks",font="70")
spaceLb=Label(root,text=" ")


#input
inputFrame=Frame(root)
lbTxt=Label(inputFrame,text="Text ")
entryText = Entry(inputFrame)
lbKey=Label(inputFrame,text="Key ")
entryKey = Entry(inputFrame)
spaceLb1=Label(inputFrame,text=" ")
lbTxt.pack()
entryText.pack()
lbKey.pack()
entryKey.pack()
spaceLb1.pack()


#Ceaser Encryption
ceaserFrame=Frame(root)
ceaserEncBtn = Button(ceaserFrame,command=Ceaser_encription,text="Ceasar Encryption")
ceaserEncLb = Label(ceaserFrame,text="Result: ")
ceaserEncBtn.pack()
ceaserEncLb.pack()


#Ceaser Decryption
ceaserDecBtn = Button(ceaserFrame,command=Ceaser_decription,text="Ceasar Decryption")
ceaserDecLb = Label(ceaserFrame,text="Result: ")
ceaserDecBtn.pack()
ceaserDecLb.pack()


#Vigenere Encription
vigenereFrame=Frame(root)
vigenereEncBtn = Button(vigenereFrame,command=Vigenere_encription,text="Vigenere Encryption")
vigenereEncLb = Label(vigenereFrame,text="Result: ")
vigenereEncBtn.pack()
vigenereEncLb.pack()


#Vigenere Decryption
vigenereDecBtn = Button(vigenereFrame,command=Vigenere_decription,text="Vigenere Decryption")
vigenereDecLb = Label(vigenereFrame,text="Result: ")
vigenereDecBtn.pack()
vigenereDecLb.pack()

#Playfair Encription
playFairFrame=Frame(root)
playFairEncBtn = Button(playFairFrame,command=playfair_encription,text="Playfair Encryption")
playFairEncLb = Label(playFairFrame,text="Result: ")
playFairEncBtn.pack()
playFairEncLb.pack()


#playFair Decryption
playFairDecBtn = Button(playFairFrame,command=playfair_decription,text="Playfair Decryption")
playFairDecLb = Label(playFairFrame,text="Result: ")
playFairDecBtn.pack()
playFairDecLb.pack()


#des Encription
desFrame=Frame(root)
desEncBtn = Button(desFrame,command=Des_encription,text="Des Encryption")
desEncLb = Label(desFrame,text="Result: ")
desEncBtn.pack()
desEncLb.pack()



#des Decryption
desDecBtn = Button(desFrame,command=Des_decription,text="Des Decryption")
desDecLb = Label(desFrame,text="Result: ")
desDecBtn.pack()
desDecLb.pack()



welcomeLb.pack()
spaceLb.pack()
inputFrame.pack()
ceaserFrame.pack()
vigenereFrame.pack()
playFairFrame.pack()
desFrame.pack()
handlingLb.pack(side=BOTTOM)



root.mainloop()


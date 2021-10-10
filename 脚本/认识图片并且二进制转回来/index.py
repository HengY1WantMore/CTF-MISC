flag_dic = ""
 
white = open(r"./gif/0.jpg","rb").read() 
black = open(r"./gif/1.jpg","rb").read()

for i in range(104):
    with open(r"./gif/%d.jpg"%i,"rb") as f:
        if f.read() == white:
            flag_dic += "0"
        else:
            flag_dic += "1"
flag = ""
     
for i in range(len(flag_dic)//8):
    flag += chr(int(flag_dic[i*8:(i+1)*8],2))
     
print(flag)

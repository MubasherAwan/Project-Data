# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:23:51 2022

@author: iammu
"""

# import socket 
# host ='localhost'
# port=2022

# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect_ex((host,port))

# message='HeY Server !!! What will we do today in lab???'
# while True:
#   s.send(message.encode('utf-8'))
#   data=s.recv(1024)
#   print("Recieved from the Server : ",str(data.decode('utf-8')))
#   reply=input('\nDo you want to Continue(y/n) : ')
#   if reply=='y':
#     continue
#   else:
#     print("Bye Server")
#     break
# s.close()

#____________Sundas Code__________

#___Creating File __________
# import pandas as pd

# # data = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/Data/Taqreeb ul Thazeeb.xlsx")
# data=pd.read_excel("TaqreebUlThzeebV2.xlsx")
# ab=str(data.Data[2])
# for i in range(3,50):
#     if(type(data.IndexNumber[i])==str):
#         ab=ab+"\n"+str(data.Data[i])

# file=open("C:/Users/iammu/OneDrive/Desktop/ab.txt","w",encoding='utf-8')
# file.write(ab)
# file.close()

#________________Code



word=["الصحابة" ,"أوثق الناس","أثبت الناس","ثقة","ثبت ثبت","ثقة","حافظ","عدل ضبط","ثقة","متقن","حجة","حافظ","ثبت","عدل","صدوق","لا بأس به","ليس به بأس","صدوق بهم","صد وق يخطئ" ,"صد وق له أوهام","صد وق سيءالحفظ","صد وق يخطئ كثيرا","صد وق تغير بآخرة","رُمى بنوع من البدعة كالتشيع أوالقدرأوالإرجاء","مقبول","لين الحديث","مستور","مجهول الحال","لايعرف حله","ضعيف","ليس بالقوي","فيه ضعف","ضعيف الحفظ","مجهول-","أي مجهول العين-,لا يعرف","متروك الحديث","واهى الحديث","ساقط","منكرالحديث","متهم بلكذ ب","كذاب"]

#words=[أوثق الناس','أثبت الناس','ثقة','ثبت ثبت','ثقة','حافظ','عدل ضبط','ثقة','متقن','حجة','حافظ','ثبت','عدل','صدوق','لا بأس به','ليس به بأس','صدوق بهم','صد وق يخطئ' ,'صد وق له أوهام','صد وق سيءالحفظ','صد وق يخطئ كثيرا','صد وق تغير بآخرة','رُمى بنوع من البدعة كالتشيع أوالقدرأوالإرج'اء','مقبول','لين الحديث','مستور','مجهول الحال','لايعرف حله','ضعيف','ليس بالقوي','فيه ضعف','ضعيف الحفظ','مجهول-','أي مجهول العين-,لا يعرف','متروك الحديث','واهى الحديث','ساقط','منكرالحديث','متهم بلكذ ب','كذاب]
#wor=["كذاب"]
#words ="كان, من'''
def listToString(s):
   
    # initialize an empty string
    str1 = ""
   
    # traverse in the string  
    for ele in s:
        str1 += ele  
   
    # return string  
    return str1
numb=0
f = open ('C:/Users/iammu/OneDrive/Desktop/ab.txt',"r",encoding='utf-8')
lines = f.readlines()
for s in lines:
    numb=numb+1
    print ('\ns'+str(numb)+' is ', s)
    tk = s.split(' ')
    nm = 0
    hukam = []
    name=[]
    btrue = False
    for i in range(len(tk)):
        if (tk[i]=="من" or tk[i]=="كان" ) and btrue ==False:#x= tk.index("من")
              btrue = True
              print ("من or كان" , i)
             
              for j in range(i-1,-1,-1):
                  h=False
                  for k in word:
                 
                      if (tk[j].strip()==k.strip()):
                          print (k,j)
                          h=True
                          hukam.append(tk[j])
                          break
                  if (h==False):
                      #print(tk[j])
                      name.append(tk[j])
                 
name.reverse()
#name = listToString(name)
nm=""
for i in name:
    nm+=i.strip()+" "
print (nm)
#res=name[::-1]
#print("\n",res,"\n")

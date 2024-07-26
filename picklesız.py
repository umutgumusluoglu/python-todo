import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--cumle", nargs="+", action="append", dest="cumle",help='cumleyi yaz')
parser.add_argument('-s','--silincek',nargs='+',action='append',dest='silincek',help='tamamlanan elemanı yaz')
args=parser.parse_args()
list = [item for sublist in args.cumle for item in sublist]
liste2= [item for sublist in args.cumle for item in sublist]

cumle=''
for i in list:
     cumle=cumle+' '+i


cumle+='\n'
cumle2=''
for i in liste2:
  cumle2=cumle2+' '+i

cumle2+='\n'


dosya=open('yeni.txt','a')
dosya.write(cumle)
dosya.close()


def oku():
 okuma=open('yeni.txt','r')
 line=okuma.readline()
 while line!='':
     print(line)
     line=okuma.readline()
 okuma.close()


def silim():
 okuma=open('yeni.txt','r')
 line=okuma.readline()
 liste=[]
 
 while line!='':
    liste.append(line)
    line=okuma.readline()
    

 okuma.close
 for a in range(len(liste)):
    if cumle2==liste[a]:
       liste.pop(a)
    
 yazma=open('yeni.txt','w')
 for a in liste:
    
    yazma.write(a)
 
oku()
silim()


   
   



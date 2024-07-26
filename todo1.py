import pickle
import argparse
def okuma():
    okuma=open('deneme.txt','rb')
    dizi=[]
    dizi=pickle.load(okuma).split('/n')
    a=''
    for i in dizi:
         
         a=i
         print(a)
        
    okuma.close()
islem=open('deneme.txt','ab')
parser = argparse.ArgumentParser(description='listeyi doldurunuz: ')
parser.add_argument("--option", nargs="+", action="append", dest="options",help='cumleyi yaz')
args=parser.parse_args()
list = [item for sublist in args.options for item in sublist]

cumle=''
for i in list:
     cumle=cumle+' '+i


pickle.dump(cumle,islem)
islem.close()

okuma()







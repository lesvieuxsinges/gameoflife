import urllib3
import re
import os

http = urllib3.PoolManager()

#DELETES EVERY STRUCTURE FILE
def filedeleter():
    for i in '1abcdefghijklmnopqrstuvwxyz':
        r = str(http.request('GET', 'https://conwaylife.com/ref/lexicon/lex_'+i+'.htm').data)
        objects = re.findall('<a name=.*?>:</a>', r)
        for i in objects:
            a = i
            i = i[8:-6]
            try:
                os.remove('structures/'+i+'.txt')
                print(i, 'deleted')
            except:
                pass
            a = a[10:-6]
            try:
                os.remove('structures/'+a+'.txt')
                print(a, 'deleted')
            except:
                pass

if __name__=="__main__":
    filedeleter()

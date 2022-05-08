import urllib3
import re

#GENERATES FILES FOR STRUCTURES
def filegenerator():
    http = urllib3.PoolManager()
    for i in '1abcdefghijklmnopqrstuvwxyz':
        r = str(http.request('GET', 'https://conwaylife.com/ref/lexicon/lex_'+i+'.htm').data)
        objects = re.findall('<a name=.*?>:</a>.*?<pre>.*?</pre>', r)
        for k in objects:

            if i=='1':
                n=2
            else:
                n=0

            name = re.findall('<a name=.*?>:</a>',k)[0][8+n:-6]
            structure = re.findall('<pre>.*?</pre>',k)[0][11:-10].replace('O','1').replace('.','0')
            structure = structure.split('\\r\\n\\t')
            createfile(name, structure)

def createfile(name,structure):
    print(name, ' downloaded')
    f = open('structures/'+name+'.txt','w')
    for line in structure:
        f.write(line+'\n')
    f.close()
if __name__=="__main__":
    filegenerator()

def makestructure(i,j, array, carte):
    for k in range(len(array)):
        for l in range(len(array[0])):
            carte[j+k][i+l]=int(array[k][l])

def structurefromfile(i,j, name, carte):
    f = open('structures/'+name+'.txt','r')
    array = [list(i[:-1]) for i in f.readlines()]
    f.close()
    makestructure(i,j, array, carte)

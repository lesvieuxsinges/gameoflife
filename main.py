import structuresmaker
import webscraper
import random
import tkinter as tk
import deleter

#PASSES THE GAME OF LIFE MAP FROM T TO T+1
def refresh(carte, x, y):
    new_carte = []
    for j in range(y):
        current = []
        for i in range(x):
            fl = []
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if j+k>=0 and i+l>=0:
                        try:
                            fl.append(carte[j+k][i+l])
                        except:
                            fl.append(0)
                    else:
                        fl.append(0)
            fl = sum(fl)-carte[j][i]
            if (fl==3 and carte[j][i]==0) or (fl==3 and carte[j][i]==1) or (fl==2 and carte[j][i]==1):
                current.append(1)
            else:
                current.append(0)
        new_carte.append(current)
    return new_carte

#FOR DEBUGGING USES, SHOWS THE MAP
def repr(carte):
    return ('\n'.join([''.join([str(i) for i in j]) for j in carte]))

#CREATES VERTICAL AND HORIZONTAL LINES ALL ACROSS THE SCREEN
def damier():
    ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    while c_x != x:
        mainframe.create_line(c_x,0,c_x,y,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != y:
        mainframe.create_line(0,c_y,x,c_y,width=1,fill='black')
        c_y+=c

#BLACK SQUARE FOR ALIVE CELLS
def black_rectangle(i,j):
    mainframe.create_rectangle(10*i,10*j,10*(i+1),10*(j+1), fill='black')

#WHITE SQUARE FOR DEAD CELLS
def white_rectangle(i,j):
    mainframe.create_rectangle(10*i,10*j,10*(i+1),10*(j+1), fill='white')

#REFRESHING THE SCREEN
def play():
    global carte
    mainframe.delete('all')
    damier()
    for j in range(y):
        for i in range(x):
            if carte[j][i]==1:
                black_rectangle(i,j)
            else:
                white_rectangle(i,j)

#FOR TKINTER
def go():
    global carte
    global refresh_time
    play()
    carte = refresh(carte,x ,y)
    root.after(refresh_time,go)

#FOR USERS

#ASKS FOR DOWNLOAD BY WEBSCRAPER
def download_resources():
    first_use = input('Do you want to download structures by webscraping (if this is your first use of the program, you probably want to)[O/N] >>>')
    if first_use == 'O':
        print('Welcome! We are downloading 693 structures for you to have fun in the Game of Life !')
        print('Loading ...')
        webscraper.filegenerator()
    if first_use == 'N':
        print('Welcome back!')
        print('Have fun !')
    else:
        download_resources()

#ASKS FOR DELETING EVERY STRUCTURE FILE
def delete_resources():
    param = input('Do you want to delete all the structures files (not to use most of the time)[O/N] >>>')
    if param == 'O':
        print('DELETING EVERYTHING')
        deleter.filedeleter()
    if param == 'N':
        return None
    else:
        delete_resources()

#ASKS FOR INT
def askint(param):
    try:
        inputed = int(input(param))
    except:
        inputed = askint(param)
    if inputed<=0:
        inputed = askint(param)
    return inputed

#ASKS FOR STRUCTURE
def structuring():
    global carte
    name = input('Enter the name of the structure >>> ').replace(' ','').lower()
    i = askint('Enter the minimal horizontal coordinate of the structure >>> ')
    j = askint('Enter the minimal vertical coordinate of the structure >>> ')
    try:
        structuresmaker.structurefromfile(i,j,name,carte)
        list_of_structures.append([i,j,name])
        print(name, 'built')
    except:
        print(name, 'does not exist')
        structuring()

#ASKS FOR GAME PARAMETERS
print("PARAMETERS")
download_resources()

delete_resources()

print('Back to cool parameters')

x = askint('Enter the horizontal size of the screen x >>> ')
y = askint('Enter the vertical size of the screen y >>> ')

carte = [[0 for i in range(x)] for j in range(y)]
size = (x,y)
c=10
list_of_structures = []

refresh_time = askint('Refresh time (ms) (advised between 1 and 10) >>> ')

structure_number = askint('How many structures do you want to put >>> ')

#CREATES STRUCTURES
for i in range(structure_number):
    structuring()

#CREATES TKINTER WINDOW
root = tk.Tk()
root.geometry(str(10*x)+'x'+str(10*y)+'+50+50')
mainframe = tk.Canvas(root, width=10*x, height=10*y, bg='white')


#MAKES THE FIRST RENDERING
damier()
mainframe.pack()
#LAUNCHES THE LOOP
go()
root.mainloop()

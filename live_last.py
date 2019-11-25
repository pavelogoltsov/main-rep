from tkinter import*
import time,copy
c = Canvas(width=900,height=700,bg='moccasin')
c.pack()
massiv_krugov=[0]*91
for h in range(90):
    massiv_krugov[h]=[0]*71
A=[0]*91
for h in range(90):
    A[h]=[0]*71

def nat(event):
    global massiv_krugov,A
    X=event.x
    Y=event.y
    nom=(X-2)//15
    nom2=(Y-2)//15
    print(nom,nom2)
    massiv_krugov[nom][nom2] = c.create_oval(nom*15+2,nom2*15+2,nom*15+17,nom2*15+17,fill='red')
    A[nom][nom2] = 1
    c.bind("<Button-2>",kolo)
def kolo(event):
    global massiv_krugov,A,B
    c.unbind("<Button-1>",a)
    
    for i in range(10):
        for j in range(10):
            print(A[i][j],' ',sep ='',end='')
        print()
    B = copy.deepcopy(A)
    while 1:
        for i in range(1,89):
            for j in range(1,69):
                if A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i+1][j+1]+A[i+1][j-1]>3:
                    B[i][j]=0
                elif A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i+1][j+1]+A[i+1][j-1]<2:
                    B[i][j]=0
                elif A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j+1]+A[i+1][j]+A[i+1][j+1]+A[i+1][j-1] == 3:
                    B[i][j] = 1
        A = copy.deepcopy(B)
        for i in range(1,89):
            for j in range(1,69):
                if A[i][j] == 1:
                    if massiv_krugov[i][j] ==0:
                        massiv_krugov[i][j] = c.create_oval(i*15+2,j*15+2,i*15+15+2,j*15+15+2,fill='red')
                else:
                    c.delete(massiv_krugov[i][j])
                    massiv_krugov[i][j] = 0
                   
        time.sleep(0.002)
        c.update()
for i in range(89):
    for j in range(69):
        c.create_rectangle(i*15+2,j*15+2,i*15+15+2,j*15+15+2,fill='moccasin')

a=c.bind("<Button-1>",nat)
mainloop()

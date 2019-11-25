from tkinter import*

root = Tk()
c = Canvas(root, width=610,height=610,bg='moccasin')
c.pack()
a=[0]*40
for i in range(40):
    a[i]=[0]*40    
for i in range(41):
    for j in range(41):
        l = 0
        c.create_rectangle(i*15+l,j*15+l,i*15+15+l,j*15+15+l,fill='moccasin')

hhh = []
ovals = [[0]*40 for i in range(40)]
for i in range(40):
    for j in range(40):
        r = 5
        l = 0
        ovals[i][j]=c.create_oval(j*15+r+l,i*15+r+l,j*15-r+l,i*15-r+l,fill = '',outline="moccasin", width=2)

def naz(ev): # при нажатии рисует круг и заносит в массив значение 1
    x = 15*round(ev.x/15)+2
    y = 15*round(ev.y/15)+2
    i,j = y//15,x//15
    #print(a[i][j],i,j)
    if a[i][j]==0:
        a[i][j]=1
        c.itemconfig(ovals[i][j],fill = "red",outline="red")
    else:
        a[i][j]=0
        c.itemconfig(ovals[i][j],fill = "",outline="moccasin")
"""def searc():
    global A,X,Y
    for j in range(40):
        for i in range(40):
            if A[i][j] ==1:
                X=j
                Y=i
                print()
                print('searc отработал, результат    ',X,Y)
                print('Самая левая точка:   ','[',j,';',i,']')
                return()"""
def obrab(event):
    FindClosedPolys(a)
#######==========================================

def FindClosedPolys(a):
    global hui
    res = list()
    print("Начал.....")
    for i in range(40):
        for j in range(40):
            if a[i][j]==1:
                res.append(Closed(a,[i,j]))
                #print('='*10,'='*10,'='*10,'='*10,sep='\n')
                #print("Closed завершила свою раюоту!!!!!")
                #print('='*10,'='*10,'='*10,'='*10,sep='\n')
    print(res)
    for i in range(40):
        for j in range(40):
            if a[i][j]>=1: a[i][j]=1
    hui = res[0][0]
    print('hui  ',hui)
    out(None,None,False)
    for cl in res:
        if len(cl) > 0:
            # рисую
            k = 15
            for h in cl:
                lines = list()
                for n in range(0,len(h)):
                    lines.append(c.create_line(h[n-1][1]*k,h[n-1][0]*k,h[n][1]*k,h[n][0]*k,width=2,fill="blue"))
                c.update()
                input()
                for i in lines:
                    c.delete(i)
                #c.create_line(h[0][1],h[0][0],h[-1][1],h[-1][0],width=2,fill="blue")

def out(now,last, withit= True):
    for i in range(40):
        for j in range(40):
            if a[i][j] == 0:
                c.itemconfig(ovals[i][j],fill="",outline="moccasin")
            if a[i][j] == 1:
                c.itemconfig(ovals[i][j],fill="red",outline="red")
            if a[i][j] == 2:
                c.itemconfig(ovals[i][j],fill="pink",outline="pink")
    if withit:
        c.itemconfig(ovals[last[0]][last[1]],fill="green")
        c.itemconfig(ovals[now[0]][now[1]],fill="blue")
    c.update()

def Closed(a,now):
    closed = list()
    seps = [0]*64
    coords = list()
    ind = -1
    last=now
    while True:
        #print("Проход...")
        a[now[0]][now[1]] = 2
        if now not in coords:
            coords.append(now)
        out(now,last)
        #input()

        
        near = Nearly(a,now,last)
        last = now
        #print('   '.join(map(str,near)))
        if len(near) == 0:
            # возвращаемся
            if ind >= 0:
                now = seps[ind]
                coords = coords[:coords.index(seps[ind])]
                ind -= 1
                continue
            else:
                print("#1")
                return closed
        # len(near) != 0
        # надо проанализировать near - что там вообще есть
        # 1 шаг: посмотреть, есть ли замыкания - если есть, то добавить
        for i in near:
            if f(i) == 2 and i in coords:
                start = coords.index(i)
                if len(coords) - start <= 3:
                    # не рассматриваю замыкания, меньшие 4
                    continue
                # Надо добавить в closed
                closed.append(coords[start:])
        # 2 шаг: посмотреть, можно ли двигаться вперед.
        #        если 1иц несколько, то повышаю стек, иначе тупо иду
        #        если 1иц нету, то возвращаюсь
        one_count = 0
        one_index = None
        for i in near:
            if f(i) == 1:
                one_count += 1
                if one_count == 1:
                    one_index = i
        if one_count == 0:
            if ind >= 0:
                now = seps[ind]
                coords = coords[:coords.index(seps[ind])]
                ind -= 1
                continue
            else:
                print("#2")
                return closed
        if one_count == 1:
            now = one_index
            continue
        else:
            #one_count > 2
            ind += 1
            seps[ind] = now
            now = one_index
        

def f(ij):
    if 0<=ij[0]<40 and 0<=ij[1]<40:
        return a[ij[0]][ij[1]]
    else:
        return 0
        
##    while len(near)>0:
##        coords.append(now)
##        a[now[0]][now[1]] = 2
##        for n in near:
##            if a[n[0]][n[1]] == 2:
##                if [n[0],n[1]] in coords:
##                    return coords[coords.index([n[0],n[1]]):]
##            elif a[n[0]][n[1]]==1:
##                last=now
##                now=[n[0],n[1]]
##                break
##        else:
##            return None
##    return coords

def Nearly(a,now,last):
    res = list()
    # сначала самые ближние, потом чуть подальше
    inds=[[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
    for i in range(8):
        ind = [now[0]+inds[i][0],now[1]+inds[i][1]]
        if ind != last and f(ind)>0: res.append(ind)
    return res


#######==========================================
# pasha
def into(i,j):
    global hui
    peres=[]
    k=0
    r=0
    while i+k != 39:# move down
        
        if [i+k,j] in hui and perp('down',i+k,j) and not ([i+k-1,j] in hui and [i+k+1,j] in hui):
            r+=1
        elif ([i+k-1,j] in hui and [i+k+1,j] in hui): c.itemconfig(ovals[i+k][j],fill="cyan",outline="cyan")
        k+=1
    peres.append(r)


    
    k=0
    r=0                    
    while i-k != 0:# move up 
        if [i-k,j] in hui and perp('up',i-k,j) and not ([i-k-1,j] in hui and [i-k+1,j] in hui):
            r+=1
        elif ([i-k-1,j] in hui and [i-k+1,j] in hui): c.itemconfig(ovals[i-k][j],fill="cyan",outline="cyan")
        k+=1
    peres.append(r)

    
    k=0
    r=0                    
    while j+k != 39:# move right 
        if [i,j+k] in hui and perp('right',i,j+k) and not ([i,j+k+1] in hui and [i,j+k-1] in hui):
            r+=1
        elif ([i,j+k+1] in hui and [i,j+k-1] in hui): c.itemconfig(ovals[i][j+k],fill="cyan",outline="cyan")
        k+=1
    peres.append(r)
        
            

    k=0
    r=0                    
    while j-k != 0:# move left
        if [i,j-k] in hui and perp('left',i,j-k) and not ([i,j-k-1] in hui and [i,j-k+1] in hui):
            r+=1
        elif ([i,j-k-1] in hui and [i,j-k+1] in hui): c.itemconfig(ovals[i][j-k],fill="cyan",outline="cyan")
        k+=1
    peres.append(r)
    if 0 in peres:
        return(False)
    else:
        for l in peres:
            if l%2==1:
                return(True)
        return False

    
def vr(ev):
    global hui
    x = 15*round(ev.x/15)+2
    y = 15*round(ev.y/15)+2
    i,j = y//15,x//15
    
    
    if into(i,j):
        c.itemconfig(ovals[i][j],fill="white",outline="white")
    else:
        c.itemconfig(ovals[i][j],fill="black",outline="black")
def kuku(ev):
    global hui
    x = 15*round(ev.x/15)+2
    y = 15*round(ev.y/15)+2
    i,j = y//15,x//15
    if perp('left',i,j):
        print('yes')
    else:
        print('no')
def perp(move,i,j):
    global hui
    if move == 'up' or move == 'down':
       # if ([i,j-1] in hui and  [i,j+1] in hui) or ([i,j-1] in hui and [i+1,j+1] in hui) or ([i,j-1] and []):
        if [i-1,j-1] in hui or [i,j-1] in hui or [i+1,j-1] in hui or [i-1,j] in hui or [i+1,j] in hui :
            if [i-1,j+1] in hui or [i,j+1] in hui or [i+1,j+1] in hui or [i-1,j] in hui or [i+1,j] in hui:
                return True
        return False
    elif move == 'left' or move == 'right':
        if [i-1,j-1] in hui or [i-1,j] in hui or [i-1,j+1] in hui or [i,j+1] in hui or [i,j-1] in hui:
            if [i+1,j-1] in hui or [i+1,j] in hui or [i+1,j+1] in hui or [i,j+1] in hui or [i,j-1] in hui:
                return True
        return False
        
c.bind("<Button-2>",obrab)
c.bind("<Button-1>",naz)
c.bind("<Button-3>",vr)

root.mainloop()












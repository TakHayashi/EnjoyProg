#sud_S2.py
#sinple DF recursive solver with fast return
import sys
from os.path import basename

from swatch import startwatch
from sudq_common import v

def solve(v,n):#depth first recursive solver
    """
    v : 9 x 9 sudoku problem input and over write result on v
    n : starting point 
    """
    #internal function for solve
    def check(v, r, c, i):#chack related cells( row, column, block)
         return row(v, r, i) and column(v, c, i) and block(v, r,c, i)
    def row(v, r, i):
         return i not in v[r] #True if not used in row
    def column(v, c, i):
         return all(True if i != v[r][c] else False for r in range(9))
    def block(v, r, c, i): #17Sec faster than above
         c0 ,r0= (c // 3) * 3 , (r // 3) * 3
         return all(True if i not in v[r][c0:c0+ 3]
                  else False for r in range(r0, r0 + 3))

    global rc,rr
    rc+=1
    while n<81:
        r,c=n // 9,n % 9
        if v[r][c] == 0:break
        n+=1
    if n >=81: # solution found?
##        t=lap('5.3f')[0]
##        for i in range(9):print(v[i])  #print solution
##        print('found: '+t+'s',f' call cnt={rc:,} return cnt={rr:,}')
        return True#search remainig solutions
    for i in range(1,10):  #try 1 - 9
        if check(v,r,c,i):   #possible to place?
           v[r][c] = i     #place it
           if solve(v,n + 1) : rr+=1;return True #call myself to go next          
    v[r][c] = 0  #nothing to place here,cancel current placemen


if __name__=='__main__' :
   
    pth=sys.argv[0]
    pyname="Script="+pth
    fn=basename(pth)
    print(fn)

    rpt=7
    vsave=[[v[i][j] for j in range(9)]for i in range(9)]
    rc,rr=0,0
    lap=startwatch()
    solve(v,0)
    t=lap()[0]
    for i in range(9):print(v[i])
    print(f'1st solve. {t:5.3f}s call count={rc:,} return count={rr:,}')
    tsum=0
    tav=0
    tmin=9999
    print('t=',end='')
    #min and average time of repeat solve except 1st time
    for i in range(rpt):
        rc,rr=0,0
        v=[[vsave[i][j] for j in range(9)]for i in range(9)]
        lap=startwatch()
        solve(v,0)
        t=lap()[0]
        tsum+=t
        tav=tsum/(i+1)
        print(f' {t:5.3f}',end='')
        if t<tmin :tmin=t
    print(f'\nTmin={tmin:5.3f} Tav={tav:5.3f} rpt= {rpt:d} ')  



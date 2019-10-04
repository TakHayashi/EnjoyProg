#sud_S1.py
#by TakHayashi
#simple Depth-first recursive solver with fast return
# after traverse all possible node in tree, solve() terminate.
#usage: just run this script.
#file required: sudq_common.py  in same dir.
#file in github/TakHayashi/sudoku
import sys
from os.path import basename

from time import perf_counter
from sudq_common import v

def solve(v,n,pr=False):#depth first recursive solver
    """
    v : 9 x 9 sudoku problem input and over write result on v
    n : start cell-index (0=< n <=80).  but 0 expected
    pr : True: Whenever solution found, print result IN this function.
    """
    #---begin internal function
    def check(v, r, c, i):#check related cells( row, column, block)
        return row(v, r, i) and column(v, c, i) and block(v, r,c, i) 
    #following 3 funcs are possible to be internal of check() but not
    def row(v, r, i):
        return i not in v[r] #True if not used in row
    def column(v, c, i):
        return all(True if i != v[r][c] else False for r in range(9))
    def block(v, r, c, i): #17Sec faster than above
        c0 ,r0= (c // 3) * 3 , (r // 3) * 3
        return all(True if i not in v[r][c0:c0+ 3]
                   else False for r in range(r0, r0 + 3))
    #---end internal function
    #solve from here
    global rc,t
    rc+=1
    while n<81:
        r,c=n // 9,n % 9
        if v[r][c] == 0:break
        n+=1
    if n >=81: # finished?
       if pr:
         t1=perf_counter()-t
         for i in range(9):print(v[i])  #print solution
         print('found:','{:5.3f}'.format(t1)+'s','rc=','{:,d}'.format(rc))
       return #finished
    for i in range(1,10):  #try 1 - 9
        if check(v,r,c,i):   #possible to place?
           v[r][c] = i     #place it
           solve(v,n + 1,pr) #call myself to go next cell          
    v[r][c] = 0 #nothing to place here,cancel current placement
    #return     #removable. return to previous cell. (backtrack). 


if __name__=='__main__' :
    pth=sys.argv[0]
    pyname="Script="+pth
    fn=basename(pth)
    print(fn)

    vsave=[[v[i][j] for j in range(9)]for i in range(9)]
    rpt=7 #repeat counter for precise execution time
    
    rc=0 #recursion counter (global) 
    t=perf_counter()
    solve(v,0,True)
    t=perf_counter()-t
    print(f'1st solve end. {t:5.3f}s ncall= {rc:,d}\n') 
    tsum=0
    tav=0
    tmin=9999
    print('t=',end='')
    for i in range(rpt):
       rc=0 
       v=[[vsave[i][j] for j in range(9)]for i in range(9)]
       t=perf_counter()
       solve(v,0)
       t=perf_counter()-t
       tsum+=t
       tav=tsum/(i+1)
       print(f' {t:5.3f}',end='')
       if t<tmin :tmin=t       
    print(f'\nTmin={tmin:5.3f} Tav={tav:5.3f} rpt= {rpt:d} \n')  
    for i in range(9):print(v[i]) #confirm v initialized 

#ssolve_S2.py
#Depth First Recursive Solver with fast return

import sys
from os.path import basename
from swatch import startwatch
from nsolve_common import v

def solve(v, n):# depth first recursive solver
    #internal functions for solve
    def check(v, r, c, i):# check related cells
         return (row(v, r, i)
                 and column(v, c, i)
                 and block(v, r, c, i)
                ) 
    def row(v, r, i):
         return i not in v[r] # True if not used in row
    def column(v, c, i):
         return all(True if i != v[r][c]
                         else False for r in range(9))
    def block(v, r, c, i): # 3 x 3 box block
         c0 ,r0= (c // 3) * 3 , (r // 3) * 3
         return all(True if i not in v[r][c0:c0+ 3]
                         else False for r in range(r0, r0 + 3))

    global rc, rr
    rc += 1
    while n < 81:
        r, c = n // 9,n % 9
        if v[r][c] == 0:break # empty cell found
        n += 1
    if n >= 81: # search completed?
##        t = lap('5.3f')[0]
##        for i in range(9):print(v[i])  #print sol
##        print(f'found: {t}s call cnt={rc:,} rtrn cnt={rr:,}')
        return True
    for i in range(1, 10):  #try 1 - 9
        if check(v, r, c, i ):   #possible to place?
           v[r][c] = i     #place it
           if solve(v, n + 1) : rr += 1;return True #go next          
    v[r][c] = 0  #nothing to place here,cancel current place

if __name__ == '__main__' :
   
    pth = sys.argv[0]
    pyname = "Script=" + pth
    fn = basename(pth)
    print(fn)

    rpt = 7
    vsave = [[v[i][j] for j in range(9)] for i in range(9)]
    rc, rr = 0, 0
    lap = startwatch()
    solve(v, 0)
    t = lap()[0]
    for i in range(9): print(v[i])
    print(f'1st solve. {t:5.3f}s '
          f'call cnt={rc:,} return cnt={rr:,}')
    tsum = 0
    tav = 0
    tmin = 9999
    print('t=',end = '')
    #min and average time in solutions except 1st sol
    for i in range(rpt):
        rc, rr = 0, 0
        v = [[vsave[i][j] for j in range(9)] for i in range(9)]
        lap = startwatch()
        solve(v, 0)
        t = lap()[0]
        tsum +=t 
        tav = tsum /( i + 1)
        print(f' {t:5.3f}',end='')
        if t<tmin :tmin = t
    print(f'\nTmin={tmin:5.3f} Tav={tav:5.3f} rpt= {rpt:d} ')  



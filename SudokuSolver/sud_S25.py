#sud_s25.py
import sys
from os.path import basename

from sudq_common import v
from swatch import startwatch


def solve(v, n):  #depth first recursive solver
    global rc
    rc += 1
    while n < 81:
        r, c = n // 9, n % 9
        if v[r][c] == 0: break
        n += 1
    if n >= 81:  # finished?
        ##        for i in range(9):print(v[i])  #print solution
        ##        print('found:',lap('5.3f')[0]+'s',f'repeat={rc:,d}')
        return True  #finished
    i1, j1 = r // 3 * 3, c // 3 * 3
    cand = list(range(1, 10))
    lad = v[r] + [
        _r[c] for _r in v
    ] + v[i1][j1:j1 + 3] + v[i1 + 1][j1:j1 + 3] + v[i1 + 2][j1:j1 + 3]
    for i in range(1, 10):
        if i in lad: cand.remove(i)


##     below is slower due to flatten list by sum()
##     cand=list(s19-set(v[r]+[_r[c] for _r in v]+
##                      sum( [v[i1+ib][j1:j1+3] for ib in range(3)],[] ) ))
    for i in cand:  #try 1 - 9
        v[r][c] = i
        if solve(v, n + 1): return True  #call myself to go next cell
    v[r][c] = 0
    #return False

if __name__ == '__main__':
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
    for i in range(9):
        print(v[i])
    print(f'1st solve. {t:5.3f}s call count={rc:,} return count={rr:,}')
    tsum, tav, tmin = 0, 0, 9999

    print('t=', end='')
    #min and average time of repeat solve except 1st time
    for i in range(rpt):
        rc, rr = 0, 0
        v = [[vsave[i][j] for j in range(9)] for i in range(9)]
        lap = startwatch()
        solve(v, 0)
        t = lap()[0]
        tsum += t
        tav = tsum / (i + 1)
        print(f' {t:5.3f}', end='')
        if t < tmin: tmin = t
    print(f'\nTmin={tmin:5.3f} Tav={tav:5.3f} rpt= {rpt:d} ')

##   rc=0
##   lap=startwatch()
##   solve(v,0)
##   print('solve end.',lap('5.3f')[0]+'s',f'repeat={rc:,d}')
"""
[5, 7, 2, 8, 9, 3, 6, 4, 1]
[9, 8, 6, 1, 4, 2, 5, 7, 3]
[3, 1, 4, 6, 5, 7, 8, 9, 2]
[8, 4, 1, 9, 6, 5, 2, 3, 7]
[7, 5, 3, 2, 1, 4, 9, 8, 6]
[2, 6, 9, 3, 7, 8, 1, 5, 4]
[6, 9, 5, 7, 3, 1, 4, 2, 8]
[1, 3, 8, 4, 2, 9, 7, 6, 5]
[4, 2, 7, 5, 8, 6, 3, 1, 9]
found: 0.859s repeat=209,185
solve end. 0.867s repeat=209,185
"""

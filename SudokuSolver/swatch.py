#swatch.py
#by TakHayashi
#execution time measurement module by closure.
#usage: see test code in __main__ of this.
from time import perf_counter,time,process_time
#don't use process_time : resolution > 16ms
def startwatch():
    begin = perf_counter()
    last = begin

    def lap(form=None):
        nonlocal begin, last
        now = perf_counter()
        fromstart = now-begin
        fromlast = now-last
        last = now
        if form:
            return '{1:{0}}'.format(form, fromstart), '{1:{0}}'.format(form, fromlast)
        else:
            return fromstart, fromlast
    return lap

#for test
if __name__ == '__main__':
    N=1000000
    lap = startwatch()
    lap2 = startwatch()
    print(id(lap), id(lap2))
    for i in range(N):
        pass

    t, dt = lap()
    print(t, dt)

    for i in range(N):
        pass

    t, dt = lap('5.3f')
    print(t, dt)

    for i in range(N):
        pass

    t, dt = lap('7.5f')
    print(t, dt)

    t, dt = lap2()
    print(t, dt)

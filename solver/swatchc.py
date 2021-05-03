#swatchc.py
#by TakHayashi
#execution time measurement module by class.
#usage: see test code in __main__ of this.

from time import process_time # or clock,time

def startwatch():
    begin = process_time()
    last = begin

    def lap(form=None):
        nonlocal begin, last
        now = process_time()
        fromstart = now-begin
        fromlast = now-last
        last = now
        if form:
            return '{1:{0}}'.format(form, fromstart), '{1:{0}}'.format(form, fromlast)
        else:
            return fromstart, fromlast
    return lap


if __name__ == '__main__':
    lap = startwatch()
    lap2 = startwatch()
    print(id(lap), id(lap2))
    for i in range(1000000):
        pass

    t, dt = lap()
    print(t, dt)

    for i in range(1000000):
        pass

    t, dt = lap('5.3f')
    print(t, dt)

    for i in range(1000000):
        pass

    t, dt = lap('7.5f')
    print(t, dt)

    t, dt = lap2()
    print(t, dt)

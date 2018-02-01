import random
from array import array
import sys
sys.setrecursionlimit(1000000)

n = 0


def init():
    pg = array('i', (0 for i in range(16)))
    pg[random.randint(0, 15)] = 2
    return pg


def print_array(pg):
    fmt=''

    for i in range(4):
        for j in range(4):
            print('%4d' % pg[i*4+j], end='')
        print('\n')


def move_ld(pg):
    n=0
    for i in range(4):
        if pg[-(i + 1)] != 0:
            n += 1
            if -(i + 1) != -n:
                pg[-n] = pg[-(i + 1)]
                pg[-(i + 1)] = 0
    return n


def move_ru(pg):
    n=0
    for i in range(4):
        if pg[i] != 0:
            n += 1
            if i!=(n-1):
                pg[n-1] = pg[i]
                pg[i] = 0
    return n



def cal_ld(pg,n):
    n=move_ld(pg)
    j=-1
    i=-2
    m=0
    while i >= -n and m<5:
        if pg[j]==pg[i]:
            pg[j]*=2
            pg[i]=0
            m+=1
            cal_ld(pg,n)
        else:
            j-=1
            i-=1
            m+=1
    return pg

def cal_ru(pg,n):
    n=move_ru(pg)
    j=0
    i=1
    m=0
    while i<n and m<5:
        if pg[j]==pg[i]:
            pg[j]*=2
            pg[i]=0
            m+=1
            cal_ru(pg,n)
        else:
            j+=1
            i+=1
            m+=1
    return pg

def over(pg):
    for i in range(16):
        if pg[i]==0:
            return 1
    for i in range(4):
        for j in range(4):
            if pg[i*4+j]!=pg[i*4+j+1] and pg[i*4+j]!=pg[i*4+j+4]:
                return 0
            else:
                return 1

def goon(pg):
    for i in range(16):
        if pg[i]==0:
            a=random.randint(0,15)
            while pg[a]!=0:
                a=random.randint(0,15)
            pg[a]=2
            break
    return pg


if __name__=='__main__':
    pg=init()
    while(over(pg)):
        print_array(pg)
        print('please input the move:a, w, s or d')
        m=input()
        if m=='a':
            for i in range(4):
                #n = move_ru(pg[(i * 4):(i * 4 + 4)])
                pg[(i * 4):(i * 4 + 4)]=cal_ru(pg[(i*4):(i*4+4)],n)
            goon(pg)
        elif m=='w':
            for i in range(4):
                #n = move_ru(pg[i::4])
                pg[i::4]=cal_ru(pg[i::4],n)
            goon(pg)
        elif m=='d':
            for i in range(4):
                #n = move_ru(pg[(i * 4):(i * 4 + 4)])
                pg[(i * 4):(i * 4 + 4)]=cal_ld(pg[(i*4):(i*4+4)],n)
            goon(pg)
        elif m=='s':
            for i in range(4):
                #n = move_ru(pg[i::4])
                pg[i::4]=cal_ld(pg[i::4],n)
            goon(pg)
        else:
            print('wrong move')
    print('Game Over')





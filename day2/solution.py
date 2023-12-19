
import re

def part1(lines):

    solution1=solution2=0
    

    for line in lines:
        maxr=maxg=maxb=0
        
        game, cubes=line.split(": ")
        juego= int(game[5:])
        
        for cube_set in cubes.split("; "):
            for n, color in map(str.split,cube_set.split(", ")):
                
                n=int(n)
                
                if color== 'red':
                    maxr=max(n,maxr)
                elif color== 'green':
                    maxg=max(n,maxg)
                elif color=='blue':
                    maxb=max(n,maxb)
            
        solution1 += juego * (maxr<=12 and maxg<=13 and maxb<=14)
        solution2 += maxb*maxr*maxg
        
        
    print('Parte 1:', solution1)
    print('Parte 2:', solution2)
                
                    
                


def part2(lines):
    pass

if __name__ == '__main__':
    with open(r'day2\input1.txt','r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
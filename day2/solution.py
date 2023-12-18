
import re

def part1(lines):
    # red,green,blue 
    colores=[12,13,14]

    contador=0

    for line in lines:
        split=line.split(":")
        juego= re.findall("\d",split[0])


def part2(lines):
    pass

if __name__ == '__main__':
    with open(r'day2\adventofcode.com_2023_day_2_input.txt','r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
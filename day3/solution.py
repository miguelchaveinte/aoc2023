def part1(lines):
    # red,green,blue 
    grid = list(map(str.rstrip, lines))
    height, width = len(grid), len(grid[0])
    
    solution1=0
    
    print(grid)
    
    print('----------')
    
    for i,j in enumerate(grid):  #enumerate me da 
        print(i,j)
    
    
    
                

def part2(lines):
    pass

if __name__ == '__main__':
    with open(r'day3\text.txt','r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
import re

def main(path):

    # leer fichero 
    with open(path,'r') as f:
        lines = f.readlines()
        # parsear fichero
        
        numbers = [re.findall('\d',line.strip()) for line in lines]
        # calcular suma de los números

        numbers = [int(number[0]+number[-1]) for number in numbers]
        
        print(sum(numbers))


def mainPart2(path):
        
        
    
        # leer fichero 
        with open(path,'r') as f:
            lines = f.readlines()
            # parsear fichero
            lines= [mapeo(line) for line in lines]
            numbers = [re.findall('\d',line.strip()) for line in lines]
            # calcular suma de los números
    
            numbers = [int(number[0]+number[-1]) for number in numbers]
            
            print(sum(numbers))


def mapeo(line):
    diccionario = {"one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",}
    
     
    for key,value in diccionario.items():
            line = line.replace(key,str(value))
    return line


if __name__ == '__main__':
    #main(r'day1\adventofcode.com_2023_day_1_input.txt')
    #main(r'day1\test.txt')
    #mainPart2(r'day1\test2.txt')
    mainPart2(r'day1\adventofcode.com_2023_day_1_input.txt')

        
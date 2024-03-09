import random
import math as math

def read_file(file_name):
    coordinates = []
    with open(file_name, 'r') as file:
        for line in file:
            coords = line.split()
            coordinates.append([int(coords[0]), int(coords[1])])
    return coordinates

def write_file(file_name, coordinates):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('Алгоритм Джарвиса:\n')
        for coords in coordinates[0]:
            file.write(f'({coords[0]}, {coords[1]}) ')
        file.write('\n')
        file.write('Алгоритм Грэхема:\n')
        for coords in coordinates[1]:
            file.write(f'({coords[0]}, {coords[1]}) ')
        file.write('\n')
        file.write('Быстрая оболочка:\n')
        for coords in coordinates[2]:
            file.write(f'({coords[0]}, {coords[1]}) ')
        file.write('\n')
        file.write('Алгоритм Чена:\n')
        for coords in coordinates[3]:
            file.write(f'({coords[0]}, {coords[1]}) ')
        file.write('\n')
        
def write_test(file_name, data):
    with open(file_name, 'w') as file:
        for test in data:
            file.write(f'{test[0]} {test[1]}\n')
        
def generate_points(amount: int):
    coords = []
    count = 0
    size = int(math.sqrt(amount)) * 10
    while (count < amount):
        point = [random.randint(0, size), random.randint(0, size)]
        while point in coords:
            point = [random.randint(0, size), random.randint(0, size)]
        coords.append(point)
        count += 1    
    
    return coords
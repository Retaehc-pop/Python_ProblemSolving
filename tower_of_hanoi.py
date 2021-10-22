import sys


def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    tower_of_hanoi.counter += 1
    if n == 1:
        print(f'1 from {from_rod} to {to_rod}')
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f'{n} from {from_rod} to {to_rod}')
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)


tower_of_hanoi.counter = 0
tower_of_hanoi(11, 'A', 'C', 'B')
print(tower_of_hanoi.counter)

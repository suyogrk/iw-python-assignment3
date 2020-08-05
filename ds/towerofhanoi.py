# a9 - tower of hanoi
def tower_of_hanoi(disks, source, middle, target):
    if disks == 1:
        print('Move disk 1 from tower {} to tower {}.'.format(source, target))
        return

    tower_of_hanoi(disks - 1, source, target, middle)
    print('Move disk {} from tower {} to tower {}.'.format(disks, source, target))
    tower_of_hanoi(disks - 1, middle, source, target)


disks = int(input('Enter number of disks: '))
tower_of_hanoi(disks, 'A', 'B', 'C')

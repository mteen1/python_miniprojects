A = list(range(1,4))
B = []
C = []

def move(n, start, end, help):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, start, help, end)

        # Move the nth disk from source to target
        end.append(start.pop())

        # Display our progress
        print(A, B, C, '##############', sep='\n')

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, help, end, start)
# Initiate call from source A to target C with auxiliary B
move(3, A, C, B)

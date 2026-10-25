def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []


    moves = []

    def record_state():
        moves.append(f"{rod1} {rod2} {rod3}")

    def move_disks(num_disks, source, auxiliary, target):
        if num_disks == 1:
            disk = source.pop()
            target.append(disk)
            record_state()
        else:
            move_disks(num_disks - 1, source, target, auxiliary)

            disk = source.pop()
            target.append(disk)
            record_state()

            move_disks(num_disks - 1, auxiliary, source, target)

    record_state()

    move_disks(n, rod1, rod2, rod3)

    return "\n".join(moves)

# To test
print(hanoi_solver(2))
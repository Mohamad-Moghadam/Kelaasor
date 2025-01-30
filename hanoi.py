def tower_of_hanoi(desired_loops, starting_point, auxiliary, destination):

    if desired_loops == 1:
        print(f"{starting_point}>{destination}")
        return

    tower_of_hanoi(desired_loops - 1, starting_point, destination, auxiliary)
    print(f"{starting_point}>{destination}")
    tower_of_hanoi(desired_loops - 1, auxiliary, starting_point, destination)


given_number = int(input("how many? "))
tower_of_hanoi(given_number, "A", "B", "C")

#  __________ PROBLEM PROMPT ___________
# Implement Backtracking algorithm for CSPs

# INPUT (3 lines)
# LLLL
# LLLL
# LLLLL

# OUTPUT (3 lines)
# DDDD
# DDDD
# DDDDD


def main():
    # VARIABLES
    input_file = "Input1.txt"
    input_data = []

    # Setting domains
    domains = [[x for x in range(10)] for i in range(13)]
    domains[8] = [1]
    domains[0] = [x for x in range(1, 10)]
    domains[4] = [x for x in range(1, 10)]

    # Read input
    with open("test_files/" + input_file) as input_file:
        for line in input_file:
            line = line.strip()
            input_data += [x for x in line]
        input_file.close()
    print(input_data)
    print(domains)


if __name__ == "__main__":
    main()

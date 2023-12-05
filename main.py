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
from csp import CSP

NUM_AUX = 3
NUM_VAR = 13

def main():
    # VARIABLES
    input_file = "Input1.txt"
    input_data = []  # list of x (x1 - x13)
    constraints = ()

    # SET DOMAINS AND CONSTRAINTS
    domains = init_domains()            # list of domains of x1 - x13 + a1-a3
    constraints = init_constraints()    # tup of tup of vars in constraints

    # READ INPUT
    with open("test_files/" + input_file) as input_file:
        for line in input_file:
            line = line.strip()
            input_data += [x for x in line]
        input_file.close()

    csp = CSP(domains, constraints)
    print(domains)


def init_domains():
    domains = [[x for x in range(10)] for i in range(NUM_VAR + NUM_AUX)]
    domains[8] = [1]
    domains[0] = [x for x in range(1, 10)]
    domains[4] = [x for x in range(1, 10)]
    # domains of auxiliary
    domains[13] = [0, 1]
    domains[14] = [0, 1]
    domains[15] = [0, 1]
    return domains


def init_constraints():
    # x4 + x8 = x13 + 10 * a1
    # x3 + x7 + a1 = x12 + 10 * a2
    # x2 + x6 + a2 = x11 + a3
    # x1 + x5 + a3 = x10 + 10 * x9

    # Notation: x(n) --> n and a(m) --> 13 + m
    c1 = (4, 8, 13, 14)
    c2 = (3, 7, 14, 12, 15)
    c3 = (2, 6, 15, 11, 16)
    c4 = (1, 5, 16, 10, 9)
    return (c1, c2, c3, c4)


if __name__ == "__main__":
    main()

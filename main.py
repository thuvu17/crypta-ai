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
from backtrack import backtrack

NUM_AUX = 3
NUM_VAR = 13

def main():
    # VARIABLES
    input_file = "Input1.txt"
    input_data = []  # list of x (x1 - x13)
 
    # READ INPUT
    with open("test_files/" + input_file) as input_file:
        for line in input_file:
            line = line.strip()
            input_data += [x for x in line]
        input_file.close()

    print(input_data)
    # SET DOMAINS AND CONSTRAINTS
    # domains = init_domains(input_data)            # list of domains of [x1...x13, a1, a2, a3]
    # print(len(domains))
    # constraints = init_constraints()    # tup of tup of vars in constraints
    csp = CSP(input_data)
    print(len(csp.variables))
    print(csp.variables)
    print(len(csp.domains))
    print(csp.domains)
    print(csp.constraints)
    solution = backtracking_search(csp)
    # print(solution)


def backtracking_search(csp):
    return backtrack(csp, {})


if __name__ == "__main__":
    main()

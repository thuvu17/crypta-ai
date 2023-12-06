# Group members: Yongwen Lei, Thu Vu

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


def main():
    # VARIABLES
    input_file = "Input2.txt"
    input_data = []  # list of x (x1 - x13)
    output_file = "output.txt"
    output_data = ""

    # READ INPUT
    with open("test_files/" + input_file) as input_file:
        for line in input_file:
            line = line.strip()
            input_data += [x for x in line]
        input_file.close()
    
    # PERFORM SEARCH
    csp = CSP(input_data)
    solution = backtracking_search(csp)

    # WRITE OUTPUT
    write_output_file(output_file, output_data, solution, input_data)


# Call backtrack search
def backtracking_search(csp):
    return backtrack(csp, {})


# Write results from search to output file
def write_output_file(output_file, output_data, solution, input_data):
    outf = open(output_file, "w")
    # If solution found
    if solution:
        for line in range(3):
            if line == 2:
                for i in range(5):
                    output_data += f"{solution[input_data[line * 4 + i]]}"
            else:
                for i in range(4):
                    output_data += f"{solution[input_data[line * 4 + i]]}"
                output_data += "\n"
    # If no solution
    else:
        output_data += "FAILURE"
    # Write output to outf and close file
    outf.write(output_data)
    outf.close()


if __name__ == "__main__":
    main()

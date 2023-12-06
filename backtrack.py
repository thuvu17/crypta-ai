from sre_constants import FAILURE


AUX_VARS = ('a1', 'a2', 'a3')


# Implementation of backtrack algorithm
def backtrack(csp, assignment):
    # If all variables are assigned, done
    if len(assignment) == len(csp.variables):
        if check_every_var_is_consistent(csp, assignment):
            return assignment
        else:
            return FAILURE
    # Else, select the next variable to assign
    selected_var = select_unassigned_variable(csp, assignment)
    # For each value in domain, check if assignment is consistent
    for value in csp.domains[selected_var]:
        if is_consistent(csp, assignment, selected_var, value):
            assignment[selected_var] = value
            result = backtrack(csp, assignment)
            if result:
                return result
            assignment.pop(selected_var)

    return FAILURE


# Select the next unassgined variable: MRV then degree heuristic
def select_unassigned_variable(csp, assignment):
    # Apply MRV
    vars_after_MRV = do_minimum_remaining_value(csp, assignment)
    # If there is >1 variable with the same MRV, do degree heuristic
    if len(vars_after_MRV) != 1:
        selected_var = do_degree_heuristic(csp, assignment, vars_after_MRV)
    else:
        selected_var = vars_after_MRV[0]

    return selected_var


# Perform MRV
def do_minimum_remaining_value(csp, assignment):
    selected_vars = []
    min_remaining_num = 10
    # For each unassigned var, get num of legal values and compare with min
    for var in csp.variables:
        if var not in assignment:
            legal_val_num = get_legal_value_num(csp, assignment, var)
            min_remaining_num = min(legal_val_num, min_remaining_num)
    # Loop through var in domain and select the one with min MRV
    for var in csp.domains:
        if get_legal_value_num(csp, assignment, var) == min_remaining_num and var not in assignment:
            selected_vars.append(var)

    return selected_vars


# Perform degree heuristic
def do_degree_heuristic(csp, assignment, variables):
    cons_on_vars = []       # [var1, var2] --> [#constraints1, #constraints2]
    # Loop through variables, count the num of constraints associated with each
    for i in range(len(variables)):
        cons_num = 0
        for cons in csp.constraints:
            if variables[i] in cons:
                cons_num += 1
        cons_on_vars.append(cons_num)
    # Get the var with the most constraints
    max_cons_num = max(cons_on_vars)
    max_cons_index = cons_on_vars.index(max_cons_num)
    return variables[max_cons_index]


# Check if assignment is consistent with constraints
def is_consistent(csp, assignment, this_variable, this_value):
    # If there is 1 unassigned var in constraint --> consistent
    # If all vars in constraint are assigned:
    #   If constraint true  --> consistent
    #   If constraint false --> inconsistent

    # Check if the value has been used by other vars
    if this_variable not in AUX_VARS:
        for var in assignment:
            if assignment[var] == this_value and var not in AUX_VARS:
                return False
    # Check if assignment satisfy all constraints
    for con in csp.constraints:
        sub_values = []
        if this_variable in con:
            if check_all_var_is_assigned(con, assignment, this_variable):
                fetch_sub_values(sub_values, con, assignment, this_value, this_variable)
                if sub_values[0] + sub_values[1] + sub_values[2] != sub_values[3] + sub_values[4] * 10:
                    return False
    return True


# Check if all variables in constraint are assigned (except this_variable)
def check_all_var_is_assigned(cons, assignment, this_variable):
    for var in cons:
        if var not in assignment and var is not this_variable:
            return False
    return True


# Fetch values for constraint
def fetch_sub_values(sub_values, cons, assignment, this_value, this_variable):
    for var in cons:
        if var == '0':
            sub_values.append(0)
        elif var == this_variable:
            sub_values.append(this_value)
        else:
            sub_values.append(assignment[var])


# Get the number of legal value for variable this_var
def get_legal_value_num(csp, assignment, this_var):
    if this_var in AUX_VARS:
        return len(csp.domains[this_var])
    legal_val_num = 0
    for val in csp.domains[this_var]:
        been_used = False
        for var in assignment:
            if var not in AUX_VARS and val == assignment[var]:
                been_used = True
        if not been_used:
            legal_val_num += 1
    return legal_val_num


# Check if assignment is consistent with all constraints
def check_every_var_is_consistent(csp, assignment):
    for con in csp.constraints:
        if '0' in con:
            if assignment[con[0]] + assignment[con[1]] + 0 != assignment[con[3]] + assignment[con[4]] * 10:
                return False
        else:
            if assignment[con[0]] + assignment[con[1]] + assignment[con[2]] != assignment[con[3]] + assignment[con[4]] * 10:
                return False
    return True

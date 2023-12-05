NUM_AUX = 3


class CSP:
    # Initialize variables, domains, and constraints
    def __init__(self, input_data):
        self.variables = self.init_variables(input_data)
        self.domains = self.init_domains(input_data)
        self.constraints = self.init_constraints(input_data)

    # Initialize variables as a tuple
    def init_variables(self, input_data):
        variables = list(set(input_data))
        variables.extend(['a1', 'a2', 'a3'])    # auxiliaries
        return tuple(variables)     # make into tuple bcs no need to change it

    # Intialize domains as a dictionary {'L': [0, 1, 2 ...]}
    def init_domains(self, input_data):                         
        domains = {}                                                                                                                                                                                                                       
        # domains of variables
        for i in range(0, len(input_data)):
            if (i + 1) not in (1, 5, 9):
                if input_data[i] not in domains:
                    domains[input_data[i]] = [x for x in range(10)]
        domains[input_data[0]] = [x for x in range(1, 10)]
        domains[input_data[4]] = [x for x in range(1, 10)]
        domains[input_data[8]] = [1]
        # domains of auxiliary
        domains['a1'] = [0, 1]
        domains['a2'] = [0, 1]
        domains['a3'] = [0, 1]
        return domains

    # Initialize constraints as a tuple of tuple
    def init_constraints(self, input_data):
        # x4 + x8 + 0 = x13 + 10 * a1
        # x3 + x7 + a1 = x12 + 10 * a2
        # x2 + x6 + a2 = x11 + 10 * a3
        # x1 + x5 + a3 = x10 + 10 * x9

        # Notation: input_data(x-1) and a(m)
        c1 = (input_data[3], input_data[7], '0', input_data[12], 'a1')
        c2 = (input_data[2], input_data[6], 'a1', input_data[11], 'a2')
        c3 = (input_data[1], input_data[5], 'a2', input_data[10], 'a3')
        c4 = (input_data[0], input_data[4], 'a3', input_data[9], input_data[8])
        return (c1, c2, c3, c4)
class CSP:
    def __init__(self, domains, constraints):
        self.variables = [None for x in range(13)]
        self.domains = domains
        self.constraints = constraints
        self.assignments = {}
        
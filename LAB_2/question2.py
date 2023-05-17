
import random #Python has a built-in module that you can use to make random numbers.

def generate_k_sat(k, m, n):
    # Initialize an empty list to store the clauses of the formula
    formula = []

    # Generate m clauses of length k
    for i in range(m): # range o-9
        clause = []
        # Select k distinct variables (or their negations) at random
        variables = random.sample(range(1, n+1), k) #randomly selection of a specified number of items from range.
        for variable in variables:
            # For each variable, decide randomly whether to include it or its negation in the clause
            if random.random() < 0.5: #Return random number between 0.0 and 1.0:
                clause.append(variable)
            else:
                clause.append(-variable)
        # Add the clause to the formula
        formula.append(clause)

    # Return the generated formula
    return formula

# Example - 
formula = generate_k_sat(3, 10, 5)
print(formula)

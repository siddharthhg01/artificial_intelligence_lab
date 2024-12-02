from itertools import product

def extract_variables(expression):
    """Extract unique variables from an expression."""
    variables = set()
    for char in expression:
        if char.isalpha() and char.isupper():  # Assuming variables are single uppercase letters
            variables.add(char)
    return sorted(variables)

def truth_table(variables):
    """Generate all possible truth assignments for given variables."""
    return list(product([True, False], repeat=len(variables)))

def evaluate_expression(expression, assignment):
    """Evaluate the expression with the given truth assignment."""
    local_dict = dict(zip(variables, assignment))
    return eval(expression, {}, local_dict)

def check_entailment(KB, alpha):
    """Check if KB entails alpha using a truth table approach."""
    global variables
    variables = extract_variables(KB + alpha)  # Identify unique variables
    assignments = truth_table(variables)  # Generate all possible truth assignments

    for assignment in assignments:
        KB_value = evaluate_expression(KB, assignment)
        alpha_value = evaluate_expression(alpha, assignment)
        
        # If KB is True and alpha is False for any assignment, entailment fails
        if KB_value and not alpha_value:
            return False

    # If no assignment contradicts entailment, return True
    return True

# Example usage
KB = "(A and B) or (C and D)"
alpha = "A or C"

result = check_entailment(KB, alpha)
print("KB entails α:", result)

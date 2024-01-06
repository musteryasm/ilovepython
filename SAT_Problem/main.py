import random
from itertools import combinations

def problem1(a, b, c, d, e):
    clause1 = (a or (not b))
    clause2 = (c or (not b))
    clause3 = (not b)
    clause4 = ((not c) or e)
    clause5 = (a or c)
    clause6 = ((not c) or (not d))
    return clause1 and clause2 and clause3 and clause4 and clause5 and clause6

def generate_neighbor(current_assignment, bits_to_flip):
    variables = list(current_assignment.keys())
    new_assignment = current_assignment.copy()
    for variable in bits_to_flip:
        new_assignment[variables[variable]] = not new_assignment[variables[variable]]
    return new_assignment

def hill_climbing(initial_assignment, max_iterations):
    current_assignment = initial_assignment
    satisfying_assignments = []
    print("Initial Assignment:", current_assignment)
    print()
    
    for num_bits_to_flip in range(1, max_iterations + 1):
        for combo in combinations(range(len(current_assignment)), num_bits_to_flip):
            neighbor = generate_neighbor(current_assignment, combo)
            print(f"Generated Neighbor (Changing {num_bits_to_flip} bits):", neighbor)
            if problem1(**neighbor):
                current_assignment = neighbor
                satisfying_assignments.append(neighbor)
                # print("Updated Assignment:", current_assignment)
            print()
    
    return satisfying_assignments

initial_assignment = {
    'a': random.choice([True, False]),
    'b': random.choice([True, False]),
    'c': random.choice([True, False]),
    'd': random.choice([True, False]),
    'e': random.choice([True, False])
}

max_iterations = 5
satisfying_assignments = hill_climbing(initial_assignment, max_iterations)

if satisfying_assignments:
    print("\nSatisfying Assignments:")
    for assignment in satisfying_assignments:
        print(assignment)
else:
    print("No satisfying assignment found.")

# Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()
def valid(solution, dimension):
    number_enter_parentheses = 0
    number_exit_parentheses = 0
    for a_parentheses in solution:
        if a_parentheses == '(':
            number_enter_parentheses += 1
        else:
            number_exit_parentheses += 1
    return dimension // 2 >= number_enter_parentheses >= number_exit_parentheses


def display_solution(solution):
    string_result = ''
    for parentheses in solution:
        string_result += parentheses
    print(string_result)


def backtracking(solution, dimension):
    solution.append(0)
    for i in ['(', ')']:
        solution[-1] = i
        if valid(solution, dimension):
            if len(solution) == dimension:
                display_solution(solution)
            backtracking(solution[:], dimension)


if __name__ == '__main__':
    number_parentheses = int(input("Please enter the number of parentheses (even number): "))
    solution_list = []
    if number_parentheses % 2 == 1:
        print("No solutions can be generated with an odd number of parentheses!")
    else:
        backtracking(solution_list, number_parentheses)

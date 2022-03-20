# Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()
def initialize(stack, current_level):
    stack.append(0)
    stack[current_level] = 39


def successor(stack, current_level):
    if stack[current_level] < 41:
        stack[current_level] += 1
        return 1
    else:
        return 0


def valid(stack, dimension):
    number_enter_parentheses = 0
    number_exit_parentheses = 0
    for a_parentheses in stack:
        if chr(a_parentheses) == '(':
            number_enter_parentheses += 1
        else:
            number_exit_parentheses += 1
    return dimension // 2 >= number_enter_parentheses >= number_exit_parentheses


def display(stack):
    string_result = ''
    for parentheses in stack:
        string_result += chr(parentheses)
    print(string_result)


if __name__ == '__main__':
    number_parentheses = int(input("Please enter the number of parentheses (even number): "))
    if number_parentheses % 2 == 1:
        print("No solutions can be generated with an odd number of parentheses!")
    else:
        starting_level = 0
        solution_stack = []
        initialize(solution_stack, starting_level)
        while starting_level > -1:
            if starting_level <= number_parentheses - 1:
                the_successor = successor(solution_stack, starting_level)
                if the_successor:
                    validator = valid(solution_stack[:starting_level + 1], number_parentheses)
                while the_successor and not validator:
                    the_successor = successor(solution_stack, starting_level)
                    if the_successor:
                        validator = valid(solution_stack[:starting_level + 1], number_parentheses)
            if the_successor:
                if number_parentheses - 1 == starting_level:
                    display(solution_stack)
                else:
                    starting_level += 1
                    initialize(solution_stack, starting_level)
            else:
                starting_level -= 1

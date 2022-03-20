# Consider the natural number n (n<=10) and the natural numbers a1, ..., an. Determine all the possibilities to
# insert between all numbers a1, ..., an the operators + and – such that by evaluating the expression the result
# is positive.

# def compute_sum(array):
#     sum = 0
#     for index in range(len(array)):
#         sum += array[index]
#     return sum
#
#
# def is_valid(solution_array, array, n):
#     sum_of_elements = compute_sum(solution_array)
#     if sum_of_elements < 0 and (len(solution_array) == n or sum(array[len(solution_array):]) + sum_of_elements < 0):
#         return False
#     return True
#
#
# def output(solution_array):
#     string = str(solution_array[0])
#     for index in range(1, len(solution_array)):
#         if solution_array[index] >= 0:
#             string += "+"
#         string += str(solution_array[index])
#     print(string)
#
#
# def next_elem(solution_array):
#     if solution_array[-1] > 0:
#         return solution_array[-1] * -1
#     return None
#
#
# def backtracking(solution_array, array, n):
#     element = array[len(solution_array)]
#     solution_array.append(element)
#     while element is not None:
#         if is_valid(solution_array, array, n):
#             if len(solution_array) == n:
#                 output(solution_array)
#             else:
#                 backtracking(solution_array[:], array, n)
#             element = next_elem(solution_array)
#             solution_array[-1] = element
#
#
# backtracking([], [5, 4, 3, 6, 7, 2, 3], 7)

# Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()
def valid(solution):
    if len(solution) < len(numbers_array) - 1:
        return True
    elif len(solution) > len(numbers_array) - 1:
        return False
    sum = numbers_array[0]
    for index in range(0, len(solution)):
        if solution[index] == '+':
            sum += numbers_array[index + 1]
        else:
            sum -= numbers_array[index + 1]
    if sum > 0:
        return True
    return False


def display_solution(solution):
    string_result = str(numbers_array[0])
    for index in range(0, len(solution)):
        string_result += ' '
        string_result += solution[index]
        string_result += ' '
        string_result += str(numbers_array[index + 1])
    print(string_result)


def backtracking(solution, dimension):
    solution.append('')
    for i in ['+', '-']:
        solution[-1] = i
        if valid(solution):
            if len(solution) == dimension:
                display_solution(solution)
            backtracking(solution[:], dimension)


if __name__ == '__main__':
    numbers_array = [5, 4, 3, 6, 7, 2, 3]
    len_array = len(numbers_array)
    solution_list = []
    backtracking(solution_list, len_array - 1)

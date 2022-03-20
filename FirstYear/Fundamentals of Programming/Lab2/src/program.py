#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

def print_complex_list(complex_list):
    """
    complex_list: the list with the complex numbers
    """
    for index in range(0,len(complex_list)):
        if (get_imaginary(complex_list[index]))<0:
            print(str(get_real(complex_list[index]))+str(get_imaginary(complex_list[index]))+'i')
        elif (get_imaginary(complex_list[index]))>0:
            print(str(get_real(complex_list[index]))+'+'+str(get_imaginary(complex_list[index]))+'i')


def print_menu():
    print("1. Read a list of complex numbers")
    print("2. Display the list")
    print("3. Display on the console the longest sequence that observes the property:")
    print("0. Exit")


def print_properties():
    print("Please choose one of the following properties:")
    print("1. Contains at most 3 distinct values")
    print("2. Numbers having the same modulus.")


def read_list_complex(complex_list):
    """
    complex_list: the list of the complex elements
    real: The real part of each elem
    imaginar: The imaginary part of each elem
    return: -
    """
    print("How many numbers you want to add?")
    number_of_numbers=input("number=")
    for index in range(1,int(number_of_numbers)+1):
        real = input("Please enter the real part of number "+str(index)+": ")
        imaginar = input("Please enter the imaginary part of number "+str(index)+": ")
        complex_list.append({'real': int(real), 'imaginary': int(imaginar)})

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# print('Hello A2'!) -> prints aren't allowed here!


def calculate_modulus(complex_number):
    real_part = get_real(complex_number)
    imaginary_part = get_imaginary(complex_number)
    modulus_complex_number = real_part*real_part + imaginary_part*imaginary_part
    return modulus_complex_number


def distinct_property_sequence(complex_list):
    """
    complex_list: the list with the complex numbers
    return: the sequence that observes the given property in a list
    """
    intermediary_list = []         # intermediary list to ensure that the sequence will have the max lenght
    final_list = []         # the list containing the sequence
    for i in range(0,len(complex_list)):
        intermediary_list = [complex_list[i]]
        number_distinct=1
        index=i+1
        while index<len(complex_list):
            if not complex_list[index] in intermediary_list:
                number_distinct=number_distinct+1                                     # nr - the number of distinct elements
            if number_distinct<4:
                intermediary_list.append(complex_list[index])
            else:
                number_distinct=0
                if len(intermediary_list)>len(final_list):   # checking lenght to ensure the maximum lenght
                    final_list = intermediary_list.copy()
                intermediary_list = []
                break
            index=index+1
        if index == len(complex_list):
            break
    if len(intermediary_list)>len(final_list):     # necessary check 
        final_list = intermediary_list.copy()
    return final_list            


def modulus_property_sequence(complex_list):
    """
    complex_list: the list with the complex numbers
    return: the sequence that observes the given property in a list
    """
    intermediary_list = [complex_list[0]]  # intermediary list to ensure that the sequence will have the max lenght
    final_list = []                 # the list containing the sequence
    for index in range(1,len(complex_list)):
        if calculate_modulus(intermediary_list[0]) == calculate_modulus(complex_list[index]):
            intermediary_list.append(complex_list[index])
        else:
            if len(intermediary_list)>len(final_list):     # checking lenght to ensure the maximum lenght
                final_list = intermediary_list.copy()
            intermediary_list = []
            intermediary_list = [complex_list[index]]
    if len(intermediary_list)>len(final_list):         # necessary check 
                final_list = intermediary_list.copy()
    return final_list
                
                
def get_real(complex_number):
    """returns the real part of the complex number"""
    return complex_number ['real']


def get_imaginary(complex_number):
    """returns the imaginary part of the complex number"""
    return complex_number ['imaginary']



def start():
    print_menu()
    complex_list = []
    test_init(complex_list)
    user_command = input("Enter your command: ")
    while user_command !='0':
        if user_command== '1':
            read_list_complex(complex_list)
        elif user_command == '2':
            print_complex_list(complex_list)
        elif user_command == '3':
            print_properties()
            user_command = input("Enter your command: ")
            if user_command == '1':
                print_complex_list(distinct_property_sequence(complex_list))
            elif user_command == '2':
                print_complex_list(modulus_property_sequence(complex_list))
            else:
                print("Invalid command!")
        else:
            print("Invalid command!")
        print_menu()
        user_command = input("Enter your command: ")
    print("Bye bye! See you next time!")


def test_init(complex_list):
    complex_list.append({'real': 5 ,'imaginary': -3})
    complex_list.append({'real': -4,'imaginary': 1})
    complex_list.append({'real': 8,'imaginary': 2})
    complex_list.append({'real': -6,'imaginary': -7})
    complex_list.append({'real': -4,'imaginary': 1})
    complex_list.append({'real': 0,'imaginary': -1})
    complex_list.append({'real': 4,'imaginary': 4})
    complex_list.append({'real': -4,'imaginary': -4})
    complex_list.append({'real': 4,'imaginary':-4})
    complex_list.append({'real': 4,'imaginary': -4})


start()
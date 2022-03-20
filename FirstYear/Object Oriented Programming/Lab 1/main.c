//
// Created by Teo on 2/22/2021.
//
/*
 *
 *
Write a C application with a menu based console interface which solves one of the problems below.
Menu entries are expected for reading a vector of numbers from the console, solving each of the 2 required
functionalities and exiting the program.
Each requirement must be resolved using at least one function. Functions communicate via input/output parameters and
the return statement.
Provide specifications for all functions.
due in week 2.
 * 5.a. Print the exponent of a prime number p from the decomposition in prime factors of a given number n
 * (n is a non-null natural number).
 * 5.b. Given a vector of numbers, find the longest contiguous subsequence such that any two consecutive
 * elements are relatively prime.
 * 6.b. Given a vector of numbers, find the longest contiguous subsequence such that the sum of any two consecutive
 * elements is a prime number.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int relatively_prime(int first_number, int second_number)
/// This function checks if two numbers are relatively prime
/// \param first_number - the first of the numbers for the check
/// \param second_number - the second of the numbers for the check
/// \return - 1 if the numbers are relatively prime or 0 otherwise
{   if (first_number / 2 == 0 || second_number /2 == 0)
        return 0;
    while (first_number != second_number)
        if (first_number > second_number)
            first_number -= second_number;
        else
            second_number -= first_number;
    return first_number;
}

int check_if_prime(int number)
/// This functions checks if a number is prime
/// \param number - the number we want to check
/// \return - 1 if the number is prime or 0 otherwise
{
    if (number % 2 == 0)
        return 0;
    for(int i = 3; i <= number/2 && number > 1; i+=2)
        if (number % i == 0)
            return 0;
    return 1;
}

int exponent_number(int number, int prime)
/// This function computes the power at which the prime number "prime" is found in the decomposition of number
/// \param number - The number for which we want to know the power of prime in its decomposition
/// \param prime - The prime number whose power we want to find in the decomposition of the number
/// \return - The power(exponent) of prime in the decomposition of number
{
    int exponent = 0;
    while (number % prime == 0)
    {
        exponent++;
        number /= prime;
    }
    return exponent;
}

void solve_first_requirement_ui()
///Function responsible for getting the input for the first requirement and solving it
{
    int prime, number;
    printf("Please enter a prime number!\n");
    scanf("%d", &prime);
    while (check_if_prime(prime) != 1)
        {
            printf("Please enter a prime number!\n");
            scanf("%d", &prime);
        }
    printf("Please enter a positive integer!\n");
    scanf("%d", &number);
    printf("The number %d has as its divisor the number %d at the power %d \n", number, prime, exponent_number(number, prime));
}

int longest_sequence_first(const int *V, int n, int *W)
/// This functions determines and saves in W longest contiguous subsequence from V such that any two consecutive
/// elements are relatively prime.
/// \param V - The initial vector in which we want to find the longest sequence
/// \param n - The dimension of the initial vector
/// \param W - The vector in which we will save the longest contiguous subsequence
/// \return - The length of the longest contiguous subsequence
{
    int i, max_len = 0, len = 1, difference = 0;
    W[0] = V[0];
    for(i = 1; i < n; i ++)
    {
        int first_number = V[i], second_number = V[i-1];
        if (relatively_prime(first_number, second_number) == 1)
            len ++;
        else
            if (len > max_len)
            {
                difference = i - len;
                max_len = len;
                for (int j = 0; j < max_len; j++)
                    W[j] = V[difference + j];
                len = 1;
            }
            else
                len = 1;
    }
    if (len > max_len)
    {
        difference = n - len;
        max_len = len;
        for (int j = 0; j < max_len; j++)
            W[j] = V[difference + j];
    }
    return max_len;
}

int longest_sequence_second(const int *V, int n, int *W)
/// This functions determines and saves in W longest contiguous subsequence from V such that the sum of any 2
/// consecutive numbers is a prime number
/// \param V - The initial vector in which we want to find the longest sequence
/// \param n - The dimension of the initial vector
/// \param W - The vector in which we will save the longest contiguous subsequence
/// \return - The length of the longest contiguous subsequence
{
    int i, max_len = 0, len = 1, sum, difference = 0;
    for(i = 1; i < n; i++)
    {
        sum = V[i] + V[i-1];
        if (check_if_prime(sum) == 1)
            len++;
        else
            if (len > max_len)
            {
                difference = i - len;
                max_len = len;
                for(int j = 0; j < len; j++)
                    W[j] = V[j + difference];
                len = 1;
            }
            else
                len = 1;
    }
    if (len > max_len)
    {
        difference = n - len;
        max_len = len;
        for(int j = 0; j < len; j++)
            W[j] = V[j + difference];
    }
    return max_len;
}


void solve_second_requirement_ui(int dimension, int Vector[])
///This function will solve the second requirement
{
    int W[100], len;
    len = longest_sequence_first(Vector, dimension, W);
    for(int i = 0; i < len; i ++)
        printf("%d ", W[i]);
    printf("\n");
}


void solve_third_requirement_ui(int dimension, int Vector[])
///This function will solve the third requirement
{
    int W[100], len;
    len = longest_sequence_second(Vector, dimension, W);
    for(int i = 0; i < len; i ++)
        printf("%d ", W[i]);
    printf("\n");
}

void print_menu_ui() {
    printf("Welcome! These are the available commands:\n"
           "1. Read a list of numbers (vector)\n"
           "2. Print the exponent of a "
           "prime number p from the decomposition in prime factors of a given number n (n is a non-null natural number)."
           "\n"
           "3. Given a vector of numbers, find the longest contiguous subsequence such that any two consecutive "
           "elements are relatively prime.\n"
           "4. Given a vector of numbers, find the longest contiguous subsequence such that the sum of any two consecutive.\n"
           "0. Exit\n");
}

int* reading_vector(int* dimension)
{
    printf("Please enter the dimension!\n");
    scanf("%d", dimension);
    int* V = (int*)malloc(*dimension*sizeof(int));
    if (V == NULL)
        exit(1);
    for(int i = 0; i < *dimension; i++)
    {
        printf("V[%d]=", i);
        scanf("%d", &V[i]);
    }
    return V;
}

int main()
{   int user_command, dimension, read_vector = 0;
    int* V_address;
    bool are_we_done = false;
    while (!are_we_done)
    {
        print_menu_ui();
        printf("Please enter your command: ");
        scanf("%d", &user_command);
        switch (user_command) {
            case 0:
            {
                if(read_vector == 1)
                    free(V_address);
                printf("Goodbye, cruel world!");
                are_we_done = true;
                break;
            }
            case 1:
            {
                if(read_vector == 1)
                    free(V_address);
                V_address = reading_vector(&dimension);
                read_vector = 1;
                break;
            }
            case 2:
            {
                solve_first_requirement_ui();
                break;
            }
            case 3:
            {
                if (read_vector == 1)
                    solve_second_requirement_ui(dimension, V_address);
                else
                    printf("Please read a vector first!\n");
                break;
            }
            case 4:
            {
                if (read_vector == 1)
                    solve_third_requirement_ui(dimension, V_address);
                else
                    printf("Please read a vector first!\n");
                break;
            }
            default:
                printf("Invalid command!\n");

        }

    }
    return 0;
}
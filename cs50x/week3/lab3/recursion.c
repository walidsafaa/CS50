#include <cs50.h>
#include <stdio.h>

int collatz(int n);
int main(void)
{
    int n = get_int("N: ");
    printf("%i\n", collatz(n));
}

int collatz(int n)
{
    // base case
    if (n == 1)
    {
        return 0;
    }
    //even numbers
    else if ((n % 2) == 0)
    {
        return 1 + collatz(n/2);
    }
    else
    {
        return 1 + collatz(n*3 + 1);
    }
}
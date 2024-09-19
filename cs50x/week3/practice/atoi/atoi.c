#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int converted = 0;
int convert(string input)
{
    // TODO
    //Base case
    char characters[] = "0123456789";
    int numbers[] = {0,1,2,3,4,5,6,7,8,9};

    if (input == (void *)0)
    {
        return 0;
    }

    for (int i = strlen(input); i >= 0; i--)
    {
        for (int x = 0; x < 10; x++)
        {
            if (input[i] == characters[x])
            {
                converted = converted * 10 + numbers[x];
                input[i] = '\000';
                convert(input);
            }
        }

    }

    return converted;
}
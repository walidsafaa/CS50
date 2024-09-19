// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string input);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }

    printf("%s\n", replace(argv[1]));
}

string replace(string input)
{
    for (int i = 0; i < strlen(input); i++)
    {
        switch (input[i])
        {
            case 'a': case 'A':
                input[i] = '6';
                break;
            case 'e': case 'E':
                input[i] = '3';
                break;
            case 'i': case 'I':
                input[i] = '1';
                break;
            case 'o': case 'O':
                input[i] = '0';
                break;
        }
    }
    return input;
}
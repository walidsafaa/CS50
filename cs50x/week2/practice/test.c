// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(int argc, string argv[1]);

int main(int argc, string argv[])
{
    string argv[1] = get_string("What is the word you want to convert? ");

    {
        if (argv == 0 || argv > 1)
        {
            printf("Missing or more than one command-line argument\n");
            return 1;
        }
        printf("%s\n", replace(argv[1]));
    }
}


string replace(int argc, string argv[1])
{
        switch (argv[i])
        {
            case a:
                printf("6\n");
                break;
            case e:
                printf("3\n");
                break;
            case i:
                printf("1\n");
                break;
            case o:
                printf("0\n");
                break;
            case u:
                printf("u\n");
                break;
        }
}
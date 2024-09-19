#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, ");
        for(int i = 0, x = strlen(argv[1]); i < x; i++)
        {
            printf("%c", toupper(argv[1][i]));
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("incorrect command-line argument - expected: ./arg <name>\n");
        //This number for calling error and to know this kind of this error
        return 404;
    }
    //printf("%s\n", argv[0]);
}
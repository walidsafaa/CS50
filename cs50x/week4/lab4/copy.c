#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>



int main(void)
{
    char *s = get_string("Text: ");
    //stored in heap
    char *t = malloc(strlen(s) + 1);

    if (t == NULL)
    {
        return 1;
    }
    //stored in stack
    //char t[strlen(s)];

    for (int i = 0; i < strlen(s) + 1; i++)
    {
        t[i] = s[i];
    }
    t[0] = toupper(t[0]);

    printf("%s\n", s);
    printf("%s\n", t);

    free(t);
}
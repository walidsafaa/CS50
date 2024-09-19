#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string name = get_string("Name: ");
    printf("Hi, ");
    for (int i = 0, x = strlen(name); i < x; i++)
    {
        printf("%c", name[i]);
    }
    printf("\n");
}
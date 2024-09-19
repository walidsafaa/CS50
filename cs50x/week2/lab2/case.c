#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = get_string("Before: ");
    printf("After: ");
    for (int i = 0, x = strlen(name); i < x; i++)
    {
        printf("%c", toupper(name[i]));
        //if (name[i] >= 'a' && name[i] <= 'z')
        //if(islower(name[i]))
        //{
            //printf("%c", name[i] - 32);
            //printf("%c", toupper(name[i]));
        //}
        //else
        //{
            //printf("%c", name[i]);
        //}
    }
    printf("\n");
}
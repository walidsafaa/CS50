#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    FILE* myfile = fopen("phonebook.csv","a");
    if (myfile == NULL)
    {
        return 1;
    }
    char *s = get_string("Name: ");
    char *t = get_string("Phone: ");

    fprintf(myfile, "%s,%s\n", s, t);
    fclose(myfile);
}

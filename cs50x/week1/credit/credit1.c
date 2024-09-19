#include <cs50.h>
#include <stdio.h>
#include <math.h>


long getpos(void);
int main(void)
{
long number = getpos();


long test = number / 1000000000000000;
printf("%li\n", test);
}

long x;
long getpos(void)
{
    do
    {
        x = get_long("Number: ");
    }
    while (x < 0);
    return x;
}

        else if ((count == 13 && number / 1000000000000 == 4) || (count == 16 && number / 1000000000000000 == 4))
        {
            printf("VISA\n");
        }
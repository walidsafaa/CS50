#include <cs50.h>
#include <stdio.h>

int getpost(void);
int main(void)
{
    // Prompt user for required height of pyramid
    int height = getpost();
    // Make pyramid by for loop
    for (int b = 0; b < height; b++)
    {

        for (int x = height - b; x > 1; x--)
        {
            printf(" ");
        }
        int a = -1;
        do
        {
            printf("#");
            a++;
        }
        while (a < b);
        // The opposite pyramid
        printf("  ");

        int d = -1;
        do
        {
            printf("#");
            d++;
        }
        while (d < b);
        // New line in each row
        printf("\n");
    }
}
// Custom function for enter a number from 1 - 8
int x;
int getpost(void)
{
    do
    {
        x = get_int("Height: ");
    }
    while (x < 1 || x > 8);
    return x;
}
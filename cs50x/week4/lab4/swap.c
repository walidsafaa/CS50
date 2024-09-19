#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("X? ");
    int y = get_int("Y? ");

    int temp = y;
    y = x;
    x = temp;

    printf("X: %i\n", x);
    printf("Y: %i\n", y);
}
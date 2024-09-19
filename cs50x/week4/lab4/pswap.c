#include <stdio.h>
#include <cs50.h>

void swap(int *a, int *b);
int main(void)
{
    int x = get_int("X? ");
    int y = get_int("Y? ");

    swap(&x, &y);

    printf("X: %i\nY: %i\n", x, y);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
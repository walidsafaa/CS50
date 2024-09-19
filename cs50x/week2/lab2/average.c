#include <stdio.h>
#include <cs50.h>

int length;
int average(int numbers[length]);

int main(void)
{
    int count = 1;
    length = get_int("How many numbers do you want? ");
    int numbers[length];
    for(int i = 0; i < length; i++)
    {
        numbers[i] = get_int("Number %i:\n", count);
        count++;
    }

    printf("Average: %i\n", average(numbers));



}

int average(int numbers[])
{
    int sum = 0;
    for (int x = 0; x < length; x++)
    {
        sum = sum + numbers[x];
    }
    int calculate = sum / length;
    return calculate;
}
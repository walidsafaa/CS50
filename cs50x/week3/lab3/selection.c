#include <stdio.h>

int main(void)
{
    int numbers[] = {6,5,8,2,7,1,3,0};
    for (int i = 0; i < 8; i++)
    {
        for (int x = 0; x < 7; x++)
        {
            if (numbers[i] > numbers[i + 1])
            {
                numbers[i + 1] = numbers[i];
            }
        }
        printf("%i\n", numbers[i]);
    }
}
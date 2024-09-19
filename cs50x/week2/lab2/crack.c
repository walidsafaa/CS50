#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string text = get_string("What is the ciphertext? ");
    int length = strlen(text);
    int count = 0;
    char letter = 'a';
    char letter2 = 'A';
    int m = 0;
    for (int i=0; i < 26; i++)
    {
        for (int y = 0; y < length; y++)
        {
            if (text[y] == letter2 || text[y] == letter)
            {
                count++;
            }
        }
    if (count > 0)
    {
        printf("%c: %i\n", letter2, count);
    }
    letter++;
    letter2++;
    count = 0;
    }
}
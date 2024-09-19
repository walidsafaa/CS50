#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    char small_letters[] = "abcdefghijklmnopqrstuvwxyz";
    char big_letters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char sub_small[strlen(argv[1])];
    int count = 0;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        sub_small[i] = tolower(argv[1][i]);
        count++;
        //printf("sub: %c\n", sub_small[i]);
    }
    char sub_big[strlen(argv[1])];
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        sub_big[i] = toupper(argv[1][i]);
        //printf("sub: %c\n", sub_big[i]);
    }
    int count2 = 0;
    int count3 = 1;
    for (int i = 0; i < 26; i++)
    {
        if (sub_small[i] == sub_small[count3] || sub_small[i] == sub_big[count3] || sub_small[count3] == sub_big[i]
            || sub_big[count3] == sub_big[i] || isdigit(argv[1][i]))
        {
            count2++;
        }
        count3++;
    }

    if (count == 26 && count2 == 0)
    {
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0; i < strlen(plaintext); i++)
        {
            for (int x = 0; x < 26; x++)
            {
                if (plaintext[i] == small_letters[x])
                {
                    printf("%c", sub_small[x]);
                }
                else if (plaintext[i] == big_letters[x])
                {
                    printf("%c", sub_big[x]);
                }

            }
            if (!isalpha(plaintext[i]))
            {
                printf("%C", plaintext[i]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

}
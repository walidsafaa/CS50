#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char characters[] = "abcdefghijklmnopqrstuvwxyz";

int computer_score(string word);

int main(void)
{
    string com1 = get_string("Player 1: ");
    string com2 = get_string("Player 2: ");

    char computer1[strlen(com1)];
    char computer2[strlen(com2)];

    for (int i = 0; i < strlen(com1); i++)
    {
        computer1[i] = tolower(com1[i]);
    }

    for (int i = 0; i < strlen(com2); i++)
    {
        computer2[i] = tolower(com2[i]);
    }

    int score1 = computer_score(computer1);
    int score2 = computer_score(computer2);

    //printf("%i %i\n", score1, score2);
    //   TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int computer_score(string word)
{
    // TODO: Compute and return score for string
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        for (int z = 0; z < 26; z++)
        {
            if (word[i] == characters[z])
            {
                sum = sum + POINTS[z];
            }
        }
    }
    return sum;
}

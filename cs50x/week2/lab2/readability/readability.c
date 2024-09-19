#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // index = 0.0588 * L - 0.296 * S - 15.8
    //  L is the average number of letters per 100 words in the text. letter / words * 100
    //  S is the average number of sentences per 100 words in the text. sentences / words * 100
    string text = get_string("Text: ");
    int letters = count_letters(text);
    // printf("%i letters\n", letters);
    int words = count_words(text);
    // printf("%i words\n", words);
    int sentences = count_sentences(text);
    // printf("%i sentences\n", sentences);

    float L = (float) letters / (float) words * 100;
    // printf("L: %.2f\n", L);
    float S = (float) sentences / (float) words * 100;
    int index = round(0.0588 * (float) L - 0.296 * (float) S - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}

int count_letters(string text)
{
    int count = 0;
    char letter = 'a';
    char letter2 = 'A';
    for (int i = 0; i < 26; i++)
    {
        for (int x = 0; x < strlen(text); x++)
        {
            if (text[x] == letter || text[x] == letter2)
            {
                count++;
            }
        }
        letter++;
        letter2++;
    }
    return count;
}

int count_words(string text)
{
    int count = 0;
    char space = ' ';
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == space)
        {
            count++;
        }
    }
    count++;
    return count;
}

int count_sentences(string text)
{
    int count = 0;
    char period = '.';
    char exclamation = '!';
    char question_mark = '?';
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == period || text[i] == exclamation || text[i] == question_mark)
        {
            count++;
        }
    }
    return count;
}
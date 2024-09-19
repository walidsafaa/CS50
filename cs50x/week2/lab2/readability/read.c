#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void)
{
    //index = 0.0588 * L - 0.296 * S - 15.8
    // L is the average number of letters per 100 words in the text. letter / words * 100
    // S is the average number of sentences per 100 words in the text. sentences / words * 100
    float L = ((float) 65 / (float) 14 * (float) 100);
    printf("L: %.2f\n", L);
}
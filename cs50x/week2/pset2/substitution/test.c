#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(void)
{
    char small_letters[] = "abcdefghijklmnopqrstuvwxyz";
    char big_letters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    small_letters = big_letters[0];
    printf("%s\n", big_letters);
}
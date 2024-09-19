#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt name from user
    string name = get_string("What's your name? ");
    printf("Hello, %s\n", name);
}
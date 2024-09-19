#include <stdio.h>
#include <cs50.h>

// Get the change and calculate it by the loop and if conditions
int change(void);
int main(void)
{
// Prompt the change from the user
    int get_cents = change();

//Types of dollars
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;
// Calculate for the change

    int calculate_quarters = 0;
    if (get_cents >= quarter)
    {
        do
        {
            get_cents = get_cents - quarter;
            calculate_quarters++;
        }
        while (get_cents >= quarter);
    }

    int calculate_dimes = 0;
    if (get_cents >= dime)
    {
        do
        {
            get_cents = get_cents - dime;
            calculate_dimes++;
        }
        while (get_cents >= dime);
    }

    int calculate_nickels = 0;
    if (get_cents >= nickel)
    {
        do
        {
            get_cents = get_cents - nickel;
            calculate_nickels++;
        }
        while (get_cents >= nickel);
    }

    int calculate_pennies = 0;
    if (get_cents >= penny)
    {
        do
        {
            get_cents = get_cents - penny;
            calculate_pennies++;
        }
        while (get_cents >= penny);
    }

    int coins = calculate_quarters + calculate_dimes + calculate_nickels + calculate_pennies;
// Print the change owed
// New line
    printf("%i\n", coins);
}

// function for getting positive number
int x;
int change(void)
{
    do
    {
        x = get_int("Change owed: ");
    }
    while (x < 0);
    return x;
}
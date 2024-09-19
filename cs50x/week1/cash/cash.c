#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

//Types of dollars

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}
int x;
int count1 = 0;
int count2 = 0;
int count3 = 0;
int count4 = 0;

//Prompt the user for the change
int get_cents(void)
{
    do
    {
        x = get_int("Change owed: ");
    }
    while (x < 0);
    return x;
}
//count the quarters
int calculate_quarters(int cents)
{
    while (cents >= 25)
    {
        cents = cents - 25;
        count1++;
    }
    return count1;
}
//count the dimes
int calculate_dimes(int cents)
{
    while (cents >= 10)
    {
        cents = cents - 10;
        count2++;
    }
    return count2;
}
//count the nickels
int calculate_nickels(int cents)
{
    while (cents >= 5)
    {
        cents = cents - 5;
        count3++;
    }
    return count3;
}
//count the pennies
int calculate_pennies(int cents)
{
    while (cents >= 1)
    {
        cents = cents - 1;
        count4++;
    }
    return count4;
}

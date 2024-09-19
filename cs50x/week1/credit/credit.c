#include <cs50.h>
#include <stdio.h>

long getpos(void);
int main(void)
{
    // Promp the card number from the user
    long number = getpos();
    long unmultiplied = number;
    long multiplied = number;
    long ccNUM3 = number;

    // Check Card Lengh
    int count = 0;
    for (int i = 0; ccNUM3 > 0; i++)
    {
        ccNUM3 = ccNUM3 / 10;
        count++;
    }
    // printf("count: %i\n", count);

    // Luhn’s Algorithm
    //  Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits
    //  together.
    int multitotal = 0;
    long digit2;
    long multiplied2 = multiplied / 10;
    while (multiplied2 > 0)
    {
        multiplied2 = multiplied2 / 100;
        digit2 = multiplied2 % 10;
        int multidigit2 = digit2 * 2;
        int a;
        int b;
        if (multidigit2 > 9)
        {
            a = multidigit2 % 10;
            b = (multidigit2 / 10) % 10;
            multitotal = multitotal + a + b;
        }
        else
        {
            multitotal = multitotal + multidigit2;
        }
    }
    long lastdigit2 = (multiplied / 10) % 10;
    long multilastdigit2 = lastdigit2 * 2;
    int c;
    int d;
    int multitotal2;
    if (multilastdigit2 > 9)
    {
        c = multilastdigit2 % 10;
        d = (multilastdigit2 / 10) % 10;
        multitotal2 = multitotal + c + d;
    }
    else
    {
        multitotal2 = multitotal + multilastdigit2;
    }

    // printf("%i\n", multitotal);

    // Collect the unmultiplied numbers
    long lastdigit = number % 10;
    int multitotal3 = 0;
    long digit1;
    while (unmultiplied > 0)
    {
        unmultiplied = unmultiplied / 100;
        digit1 = unmultiplied % 10;
        multitotal3 = multitotal3 + digit1;
    }
    int multitotal4 = multitotal3 + lastdigit;

    // Add the sum to the sum of the digits that weren’t multiplied by 2
    int sum = multitotal2 + multitotal4;
    // printf("sum: %i\n", sum);

    // Check the type of the card
    if (sum % 10 == 0)
    {
        if (count == 16 && (number / 100000000000000 == 51 || number / 100000000000000 == 52 || number / 100000000000000 == 52 ||
                            number / 100000000000000 == 53 || number / 100000000000000 == 54 || number / 100000000000000 == 55))
        {
            printf("MASTERCARD\n");
        }

        else if ((count == 13 && number / 1000000000000 == 4) || (count == 16 && number / 1000000000000000 == 4))
        {
            printf("VISA\n");
        }

        else if (count == 15 && (number / 10000000000000 == 34 || number / 10000000000000 == 37))
        {
            printf("AMEX\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

long x;
long getpos(void)
{
    do
    {
        x = get_long("Number: ");
    }
    while (x < 0);
    return x;
}
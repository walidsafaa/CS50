#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string input = get_string("Message: ");

    int decimal[strlen(input)];
    // TODO  turning the text into decimal numbers
    for (int x = 0; x < strlen(input); x++)
    {
        decimal[x] = input[x];
        // converting them into equivalent binary numbers starting from 256 bits
        int a = decimal[x];

        if (a >= 128)
        {
            a = a - 128;
            int b = 1;
            print_bulb(b);
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 64)
        {
            a = a - 64;
            int b = 1;
            print_bulb(b);
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 32)
        {
            int b = 1;
            print_bulb(b);
            a = a - 32;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 16)
        {
            int b = 1;
            print_bulb(b);
            a = a - 16;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 8)
        {
            int b = 1;
            print_bulb(b);
            a = a - 8;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 4)
        {
            int b = 1;
            print_bulb(b);
            a = a - 4;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 2)
        {
            int b = 1;
            print_bulb(b);
            a = a - 2;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }

        if (a >= 1)
        {
            int b = 1;
            print_bulb(b);
            a = a - 1;
        }
        else
        {
            int b = 0;
            print_bulb(b);
        }
        printf("\n");
    }
}


void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

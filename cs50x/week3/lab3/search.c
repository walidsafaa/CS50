#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    typedef struct //person
    {
        string name;
        string number;
    }
    person;

    person people[3];

    people[0].name = "Walid";
    people[0].number = "05647";

    people[1].name = "Ahmed";
    people[1].number = "16556";

    people[2].name = "Mohamed";
    people[2].number = "165656";

    string name = get_string("Name: ");
    char name2[strlen(name)];
    for (int i = 0; i < 3; i++)
    {
        char name1[strlen(people[i].name)];
        for (int x = 0; x < strlen(people[i].name); x++)
        {
            name1[x] = tolower(people[i].name[x]);
        }
        for (int x = 0; x < strlen(name); x++)
        {
            name2[x] = tolower(name[x]);
        }

        if (strcmp(name1, name2) == 0)
        {
            printf("FOUND! %s\n", people[i].number);
            return 0;
        }
    }
    printf("NOT FOUND!\n");
}
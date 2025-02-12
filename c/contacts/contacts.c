// Search a pre-constructed contact list

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[3];

    people[0].name = "Jon";
    people[0].number = "+1-555-123-1010";

    people[1].name = "Jane";
    people[1].number = "+1-555-456-0202";

    people[2].name = "David";
    people[2].number = "+1-555-789-0303";

    string name = get_string("Name: ");
    for (int i = 0; i < 3; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}


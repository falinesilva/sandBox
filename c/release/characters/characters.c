// How many characters are in a name?

#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string name = get_string("Name: ");
    int length = strlen(name);
    printf("The name has %i characters.\n", length);
}
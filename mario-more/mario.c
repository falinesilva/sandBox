#include <stdio.h>
#include "cs50.h"

void print_row(int space, int hash);

int main(void)

{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        print_row(n - i, i);
    }

}

void print_row(int space, int hash)
{
    for (int i = 1; i < space; i++)
    {
        printf(" ");
    }
    for (int j = 0; j <= hash; j++)
    {
        printf("#");
    }
    printf("  ");
    for (int i = -1; i < hash; i++)
    {
        printf("#");
    }
    printf("\n");
}

// Print a pyramid

#include <cs50.h>
#include <stdio.h>

void print_row(int space, int hash);

int main(void)

{
    int n;
    do
    {
        n = get_int("Height (1-50): ");
    }
    while (n < 1 || n > 50);

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
    for (int i = -1; i < hash; i++)
    {
        printf("#");
    }
    printf("\n");
}
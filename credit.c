#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long n = get_long("Number: ");
    n = n % 10;
    printf("%li\n", n);
}

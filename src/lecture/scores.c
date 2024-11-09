#include <cs50.h>
#include <stdio.h>

// Average calculation
const int N = 3;

// Prototype
float average(int length, int array[]);

int main(void)
{
    // Get scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores [i] = get_int("Score: ");
    }
    // Print average
    printf("Average: %f", (scores[0] + scores [1] + scores [2]) / N);

}
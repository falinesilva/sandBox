#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Calculate grade level of user's text.
int grade_calc(string text);
// Constant for error message.
int main(void)
{
    int grade = 0;

    // Ask user to input text.
    string text = get_string("Type text and press Enter: \n");
    // Calculate grade level of the text.
    grade = grade_calc(text);
    grade = round(grade);

    // Print results.
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int grade_calc(string text)
{
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Calculate the amount of letters, words and senteces in the text.
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        else if (isblank(text[i]))
        {
            words++;
        }
    }

    // Calculate averages.
    float average_letters = (float) letters / words * 100;
    float average_sentences = (float) sentences / words * 100;

    // Calculate grade based on Coleman-Liau index.
    float result = 0.0588 * average_letters - 0.296 * average_sentences - 15.8 + 0.5;
    return result;
}

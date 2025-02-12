// Calculate the approximate grade level of some text

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int grade_calc (string text);
int main(void)
{
    int grade = 0;

    string text = get_string("Type text and press Enter: ");
    grade = grade_calc(text);
    grade = round(grade);

    if (grade < 1)
    {
        printf("Before Grade 1.\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", (float)grade);
    }
}

int grade_calc (string text)
{
    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters ++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences ++;
        }
        else if (isblank(text[i]))
        {
            words ++;
        }
    }

    float average_letters = (float)letters / words *100;
    float average_sentences = (float)sentences / words *100;
    
    float result = 0.0588 * average_letters - 0.296 * average_sentences - 15.8 + 0.5;
    return result;
}
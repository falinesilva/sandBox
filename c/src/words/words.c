// Two-player scrabble game

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int POINTS [] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calculate_score(string word);

int main(void)
{   
    printf ("Scrabble!\n");
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = calculate_score(word1);
    int score2 = calculate_score(word2);

    if (score1 > score2)
    {
        printf ("Player 1 Wins!");
    }
    else if (score1 < score2)
    {
        printf ("Player 2 Wins!");
    }
    else
    {
        printf ("Tie!");
    }
}

int calculate_score(string word)
{
    int score = 0;
    
    for (int i = 0; word[i] != '\0'; i++)
    {
        char letter = tolower(word[i]);
        
        if (isalpha(word[i])) 
        {
            score += POINTS[letter - 'a'];
        }
    }
    return score;
}

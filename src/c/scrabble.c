#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

// Points for each letter
int POINTS [] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Scrabble score calculator
int calculate_score(string word);

int main(void)
{
    // Prompt the user for two words
    
    string word1 = get_string("Player 2: ");
    string word2 = get_string("Player 2: ");

    // Calculate the score of each word
    int score1 = calculate_score(word1);
    int score2 = calculate_score(word2);

    // Print the high score
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
        // Converts character to lowercase.
        char letter = tolower(word[i]);
        
        //// Add scrabble points if the char is alphabetical
        if (isalpha(word[i])) 
        {
            score += POINTS[letter - 'a'];
        }
    }
    return score;
}

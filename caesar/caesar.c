#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Verify key is a single command.
bool check_key (int argc, string arg);

// Encipher a plain text input with the key.
string encipher (string plaintext, int key);

int main(int argc, string argv[])
{
    // Get key and verify.
    if (!check_key (argc, argv[1]))
    {
        printf("Error Usage: Single digit.");
        return 1;
    }

    // Convert key to integer.
    int key = atoi(argv[1]);

    // Ask user to input plaintext.
    string plain = get_string("Enter plaintext: \n");

    // Encipher plaintext.
    plain = encipher(plain, key);

    // Print ciphertext.
    printf("ciphertext: %s\n", plain);
}

string encipher (string plaintext, int secret)
{
    int n = strlen(plaintext);
    for (int i = 0; i < n; i++)
    {
        // Check if the character alphabetical and apply formula.
       if (isalpha(plaintext[i]))
        {
            if (islower(plaintext[i]))
            {
                plaintext[i] = (plaintext[i] - 'a' + secret) % 26 + 'a';
            }
            else if (isupper(plaintext[i]))
            {
                plaintext[i] = (plaintext[i] - 'A' + secret) % 26 + 'A';
            }
        }
    }
    return plaintext;
}

bool check_key (int argc, string arg)
{
    return (argc == 2 && isdigit(arg[0]) && arg[1] == '\0');
}

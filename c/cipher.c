//Create a cipher text with command-line input.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool check_key(int argc, string arg);

string encipher(string plaintext, int key);

int main(int argc, string argv[])
{
    if (!check_key(argc, argv[1]))
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    int key = atoi(argv[1]);

    string plain = get_string("Enter plaintext: \n");

    plain = encipher(plain, key);

    printf("ciphertext: %s\n", plain);
}

string encipher(string plaintext, int secret)
{
    int n = strlen(plaintext);
    for (int i = 0; i < n; i++)
    {
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

bool check_key(int argc, string arg)
{
    if (argc != 2)
        return false;

    for (int i = 0; arg[i] != '\0'; i++)
    {
        if (!isdigit(arg[i]))
            return false;
    }
    return true;
}

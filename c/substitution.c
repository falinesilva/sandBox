// Under development
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Validate Key
bool check_key(int argc, string argv);

// Encrypt
string encrypt(string p, string key);

int main (int argc, string argv[])
{
    // Get key
    string key = argv[1];
    
    // Validate key
    if (!isalpha(key));
    {
        printf("Usage: ./substitution key");
        return 1;
    }
    if (!strln(key) == 26);
    {
        printf("Key must contain 26 characters.");
        return 1;
    }
   
   // Get plaintext
    string plain = get_string("plaintext: \n");

    // Encipher
    string plain = encrypt(plain, key);

    // Print ciphertext
    printf("cipher: \n");
}

bool check_key(int argc, string argv)
{
// This section is under development.
}

string encrypt(string p, string key)
{
// This section is under development.
}
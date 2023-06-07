#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    //Get the key
    //invalid key
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    //valid key_positive_int
    string p;
    int key = atoi(argv[1]);
    if (key > 0)
    {
        //prompt the user_ plaintext
        p = get_string("Plaintext:  ");
    }
    //invalid key_negative_integer
    else
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    //output_ciphertext
    printf("ciphertext: ");
    for (int i = 0, len = strlen(p); i < len; i++)
    {
        //int c = p[i] + key;
        int c = 0;
        if (isalpha(p[i]) && isupper(p[i]))
        {
            c += ((p[i] + key - 65) % 26 + 65);
            printf("%c", c);

        }
        else if (isalpha(p[i]) && islower(p[i]))
        {
            c += ((p[i] + key - 97) % 26 + 97);
            printf("%c", c);

        }
        else
        {
            printf("%c", p[i]);
        }
    }
    printf("\n");
}

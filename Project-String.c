#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = "HI!";
     int a = strlen(s);
     for (int i = 0; i < a; i++)
     {
        printf("%i\n", s[i]);
     }
    //printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
}

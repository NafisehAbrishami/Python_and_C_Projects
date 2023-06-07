#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{

    string t = get_string("TEXT: ");
    int count = 0;
    char space = ' ' ;
    for (int i = 0, len = strlen(t); i < len; i++)
    {
        if (t[i] == ' ')
        {
            count++;
        }
        printf("%i\n", i);
    }
    printf("words:%i\n", count);
}

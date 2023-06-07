#include <cs50.h>
#include <stdio.h>
int main(void)
{
    // Prompt User Input
    string name = get_string("What is your name? ");
    printf("hello,%s\n", name);
}
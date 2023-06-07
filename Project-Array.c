#include <cs50.h>
#include <stdio.h>

int main (void)
{
    //promt
    int n = get_int("How many scores? ");
    int scores [n];
    // loop
    for (int i = 0; i < n; i++)
    {
        scores [i] = get_int("Score: ");
    }
    printf("Average: %f\n", (scores [0] + scores [1] + scores [2]) / 3.00);
}

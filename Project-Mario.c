#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user input
    int rowNO, totalrowNO, space, symbol;
    do
    {
        totalrowNO = get_int("Height: ");
    }
    while (totalrowNO < 1 || totalrowNO > 8);

    // for_row_numbers
    for (rowNO = 1; rowNO <= totalrowNO ; rowNO++)
    {
        //printf_spaces_first
        for (space = 1; space <= (totalrowNO - rowNO); space++)
        {
            printf(" ");
        }
        //printf_symbols_second
        for (symbol = 0; symbol <= (totalrowNO - space); symbol++)
        {
            printf("#");
        }
        printf("\n");
    }

}
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // prompt the user for string of text
    string text = get_string("Text: ");
    //count the number of letters
    int letters = count_letters(text);
    //count the number of words
    int word = count_words(text);
    int words = word + 1;
    //count the number of sentences
    int sentences = count_sentences(text);
    //grade_compute
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
    // print Grade 1-16+
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

// function_count_letters
int count_letters(string text)
{
    int count = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isupper(text[i]))
        {
            count ++;
        }
        else if (islower(text[i]))
        {
            count ++;
        }
    }
    return count;
}
// function_count_words
int count_words(string text)
{
    // how many spaces
    int count = 0;
    char space = ' ';
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}
// function_count_sentences
int count_sentences(string text)
{
    int count = 0;
    char endsentence[] = {'.', '!', '?'};
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == endsentence[0] || text[i] == endsentence[1] || text[i] == endsentence[2])
        {
            count++;
        }
    }
    return count;
}
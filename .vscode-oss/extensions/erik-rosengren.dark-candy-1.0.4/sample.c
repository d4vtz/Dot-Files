/* Dark Candy */
#include <stdio.h>

typedef struct Candy
{
   char *type;
   char *color;
} Candy;

Candy candies[2] = {
    {.type = "gummibears", .color = "red"},
    {.type = "chocolate", .color = "brown"}};

void PrintCandy(Candy *candy)
{
   printf("%s %s", candy->type, candy->color);
}

int main()
{
   for (int i = 0; i < sizeof(candies); ++i)
   {
      PrintCandy(&candies[i]); // Dark Candy Retro
   }
   return 0;
}
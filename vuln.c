#include <stdio.h>
#include <string.h>
#include <threads.h>
#include <mqueue.h>

 
int main(int argc, char *argv[])
{
    char buffer[8] = {0};
 
    if(argc != 2)
    {
        printf("A single argument is required.\n");
        return 1;
    }
 
    strcpy(buffer, argv[1]);
    return 0;
}
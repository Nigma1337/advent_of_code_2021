#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fp;
    int hoz = 0;
    int dep = 0;
    char buff[255];
    fp = fopen("input.txt", "r");
    while (fgets(buff, sizeof buff, fp))
    {        
        if(strstr(buff, "forward")){
            memmove(&buff[0],&buff[0+8],strlen(buff));
            hoz += atoi(buff);
        }
        else if(strstr(buff, "up")){
            memmove(&buff[0],&buff[0+3],strlen(buff));
            dep -= atoi(buff);
        }
        else if(strstr(buff, "down")){
            memmove(&buff[0],&buff[0+5],strlen(buff));
            dep += atoi(buff);
        }
    }
    printf("%i %i %i\n", dep, hoz, dep*hoz);
}
#include <stdio.h>
#include <string.h>

int main(){

    char name[25]; //bytes
    int age;

    printf("\nWhat's your name?");
    scanf("%s", &name);                 //Is used to catch the input
    fgets(name, 25, stdin);             //Can read white spaces
    name[strlen(name)-1] = '\0';        //This deactivate a funcion on fgets that puts the output in a new line

    printf("How old are you?");
    scanf("%d", &age);

    printf("\nHello %s, how are you?", name);
    printf("\nYou are %d years old", age);

    return 0;



















}
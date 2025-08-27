#include <stdio.h>
#include <stdbool.h>

int main(){

    char a = 'C';                       //single character     %c
    char b[] = "Bro";                   //array of characters  %s

    float c = 3.141592;                 //4 bytes (6-7 digits)      %f
    double d = 3.141592653589793;       //8 bytes (15-16 digits)    %lf

    bool e = true;                      //Variable bool         %d

    char f = 100;                       //1 byte We can use the value(%d) or the ascii table(%c) (-128, +127) We can omite the 'signed'
    unsigned char g = 255;          //1 byte No negative number (0-255) %d or %c
    printf("%d\n",f);
    printf("%c\n",f);

    short int h = 32767;                 //2 bytes   (-32768,+32767) %d
    unsigned short int i = 32500;        //2 bytes   No negative number (0, +65535) %d

    int j = 98099089;                            //4 bytes It really is 'long int' but we can skip the 'long' (-2147483648,+2147483648) %d
    unsigned int k = 23497324;                   //4 bytes (0, 4294967295) %d

    long long int l = 4234234556467546;                  //8 bytes (-9 quintillion,9 quintillion) %lld
    unsigned long long m = 3453454656456456U;             //8 bytes We can add an U to the end  (0, 18 quintillion) %lld

    //Format specifiers % = define and formats a type of data do be displayed 

    // %c = character 
    // %s = string
    // %f = float
    // %lf = double
    // %d = integer

    //This is to floats and doubles
    // %.1 = decimal precision
    // %1 = minimum field width 
    // %- = left align 

    float item1 = 5.75;
    printf("Item 1 : $%-8.2f\n", item1);
    printf("Item 1 : $%4.5f\n", item1);

    //C Constants = fixed value tha can not be changed (it usually declares in MAYUS)

    const float PI = 3.1415926535897932384626;
    printf("%f\n", PI);

    //Operations 
    //++ increment (sums 1 to a number)
    //-- decrement (substracts 1 to a number)

    int x = 5;
    float y = x + (float) x;
    y++;
    printf("%f\n", y);

    //aumented assigment operators = ussed to replace a statement where an operator takes a variable as one of its arguments and then assigns its result back to the same variable
    int z = 10;
    z = z + 1; 
    z+= 2; 

}










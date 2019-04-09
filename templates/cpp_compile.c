#include <stdio.h>
#include<stdlib.h>

int main(){
    system("cd C:/Users/user/Documents/000PSL && g++ -o hello hello.cpp 2> outcpp.txt");
    chdir("C:/Users/user/Documents/000PSL");
    FILE *fp;
    fp = fopen("outcpp.txt", "r");
    char ch;
    if((ch = fgetc(fp)) == EOF){
        system("hello.exe > outcpp.txt");
    }
    else {
        fp = fopen("outcpp.txt", "r");
        while((ch = fgetc(fp)) != EOF)
            printf("%c", ch);
    }
}

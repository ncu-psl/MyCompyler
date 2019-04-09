#include <stdio.h>
#include<stdlib.h>

int main(){
    system("cd C:/Users/user/Documents/000PSL && gcc -o hello hello.c 2> outc.txt");
    chdir("C:/Users/user/Documents/000PSL");
    FILE *fp;
    fp = fopen("outc.txt", "r");
    char ch;
    if((ch = fgetc(fp)) == EOF){
        system("hello.exe > outc.txt");
    }
    else {
        fp = fopen("outc.txt", "r");
        while((ch = fgetc(fp)) != EOF)
            printf("%c", ch);
    }
}

#include <stdio.h>
#include<stdlib.h>

int main(){
    system("cd C:/Users/user/Documents/000PSL && python hello.py 2> outp.txt");
    chdir("C:/Users/user/Documents/000PSL");
    FILE *fp;
    fp = fopen("outp.txt", "r");
    char ch;
    if((ch = fgetc(fp)) == EOF){
        system("python hello.py > outp.txt");
    }
    else {
        fp = fopen("outp.txt", "r");
        while((ch = fgetc(fp)) != EOF)
            printf("%c", ch);
    }
}

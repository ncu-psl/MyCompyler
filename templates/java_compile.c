#include <stdio.h>
#include<stdlib.h>

int main(){
    system("cd C:/Users/user/Documents/000PSL && javac hello.java 2> outj.txt");
    chdir("C:/Users/user/Documents/000PSL");
    FILE *fp;
    fp = fopen("outj.txt", "r");
    char ch;
    if((ch = fgetc(fp)) == EOF){
        system("java hello.java > outj.txt");
    }
    else {
        fp = fopen("outj.txt", "r");
        while((ch = fgetc(fp)) != EOF)
            printf("%c", ch);
    }
}

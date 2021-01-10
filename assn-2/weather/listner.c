#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#define BUFFER_SIZE 1024
#define TERMINATE_MESSAGE "<!#TERMINATE#!>"

int main()
{
    int fd1;
    char *myfifo = "/tmp/weatherMessage";
    mkfifo(myfifo, 0666);
    char str1[BUFFER_SIZE];
    while (1)
    {
        fd1 = open(myfifo, O_RDONLY);
        read(fd1, str1, BUFFER_SIZE);

        if (strcmp(str1, TERMINATE_MESSAGE) == 0)
        {
            printf("Broadcaster has stopped broadcasting!\nTerminating listner %d\n", (int)getpid());
            break;
        }

        printf("Weather Report: %s\n", str1);
        close(fd1);
    }
    return 0;
}
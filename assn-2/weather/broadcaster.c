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
    int fd;
    char *myfifo = "/tmp/weatherMessage";
    mkfifo(myfifo, 0666);
    char buffer[BUFFER_SIZE], temp;

    printf("Starting broadcaster..........\n");
    while (1)
    {
        fd = open(myfifo, O_WRONLY);

        // Read weather info from user
        printf("Enter Weather Report: ");
        scanf("%[^\n]s", buffer);
        scanf("%c", &temp);

        // Write weather info in FIFO
        write(fd, buffer, strlen(buffer) + 1);

        // Close FIFO
        close(fd);

        printf("Terminate (Y/N): ");
        scanf("%c", &temp);
        getchar();

        if (temp == 'y' || temp == 'Y')
        {
            fd = open(myfifo, O_WRONLY);
            write(fd, TERMINATE_MESSAGE, 16);
            printf("\nTerminating broadcasting..........\n");
            break;
        }
    }
    return 0;
}
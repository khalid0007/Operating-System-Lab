#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

// Program implements telephone conversation using fifo

int main()
{
    int fd;
    char *fifopath = "/ss/myfifo4";
    int val = mkfifo(fifopath, 0666);
    if (val == -1)
    {
        perror("Problem in fifo making \n");
    }

    char str1[80], str2[80];

    while (1)
    {
        //Open fifo for writing
        printf("Opening file to read\n");
        fd = open(fifopath, O_WRONLY);
        // if (fd == -1)
        // {
        //     printf("error in opening file\n");
        // }
        printf("Enter input\n");
        fgets(str2, 80, stdin);

        //Write to fifo
        printf("Writing in file \n");
        write(fd, str2, strlen(str2) + 1);
        close(fd);
        printf("String is %s \n", str2);

        //Open fifo for reading
        fd = open(fifopath, O_RDONLY);

        //Read from fifo
        read(fd, str1, sizeof(str1));
        printf("Receiver: %s\n", str1);
        close(fd);
    }
    return 0;
}
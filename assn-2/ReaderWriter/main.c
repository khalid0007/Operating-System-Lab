
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/wait.h>
#include <sys/mman.h>
sem_t reader_sem, writer_sem;
pthread_t tid;
pthread_t Writer[100], Reader[100];
int CurrentReader = 0;
int *database;
void *create_shared_memory(size_t size)
{
    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    return mmap(NULL, size, protection, visibility, -1, 0);
}
void *reading(void *database)
{
    int *db = database;
    sem_wait(&reader_sem);
    CurrentReader++;
    //prioritizing writer process
    if (CurrentReader == 1)
        sem_wait(&writer_sem);
    sem_post(&reader_sem);
    //printf("%d reader is inside\n",CurrentReader);
    //to allow more than 1 reader thread adding delay
    usleep(4);
    //printf("%d reader is reading DB value %d \n",CurrentReader,*db);
    sem_wait(&reader_sem);
    CurrentReader--;
    if (CurrentReader == 0)
    {
        //releasing lock
        sem_post(&writer_sem);
    }
    sem_post(&reader_sem);
    printf("%d Reader is leaving\n", CurrentReader + 1);
    return NULL;
}

void *writing(void *database)
{
    int *db = database;
    printf("Writer is trying to enter\n");
    sem_wait(&writer_sem);
    printf("Writer has entered\n");
    //*db = *db + 1;
    sem_post(&writer_sem);
    printf("Writer is leaving\n");
    return NULL;
}

int main()
{
    int numReader, numWriter, i;
    printf("Enter the number of readers:");
    scanf("%d", &numReader);
    printf("Enter the number of writers:");
    scanf("%d", &numWriter);
    printf("\n");

    database = malloc(sizeof(int));
    sem_init(&reader_sem, 0, 1);
    sem_init(&writer_sem, 0, 1);
    int mx = numReader > numWriter ? numReader : numWriter;
    for (i = 0; i < mx; i++)
    {
        if (i < numWriter)
            pthread_create(&Writer[i], NULL, writing, (void *)database);
        if (i < numReader)
            pthread_create(&Reader[i], NULL, reading, (void *)database);
    }

    for (i = 0; i < mx; i++)
    {
        if (i < numWriter)
            pthread_join(Writer[i], NULL);
        if (i < numReader)
            pthread_join(Reader[i], NULL);
    }
}
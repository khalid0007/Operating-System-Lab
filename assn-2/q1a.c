#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void iterate(int time)
{
	for (int i = 1; i <= 10; i++)
		printf("Process Id: %d Iteration: %d\n", (int)getpid(), i), sleep(time);
}

int main()
{
	pid_t pid = fork();

	if (pid == -1)
		printf("Fork failure\n");
	else if (pid == 0)
	{
		//Child process X
		printf("Child X created\n");
		iterate(1);
	}
	else
	{
		pid_t pid2 = fork();

		if (pid2 == -1)
			printf("Fork failure\n");
		else if (pid2 == 0)
		{
			//Child process Y
			printf("Child Y created\n");
			iterate(2);
		}
		else
		{
			wait(NULL);
		}
		wait(NULL);
	}

	return 0;
}
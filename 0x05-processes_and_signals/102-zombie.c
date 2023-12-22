#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - Creates an infinite loop.
 *
 * This function enters an infinite loop with a sleep duration of 1 second
 * in each iteration. It is typically used to keep a process alive.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates zombie processes.
 *
 * This function demonstrates creating zombie processes by forking
 * five child processes. The parent process prints information about
 * each child process and then enters an infinite loop to keep itself alive.
 * The child processes exit immediately, becoming zombies.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(EXIT_SUCCESS);
	}

	infinite_while();

	return (0);
}

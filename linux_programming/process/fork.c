#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void test_func(void){
  printf("this is test fucntion(pid %d)\n", getpid());
}
int main(int argc, char **argv){
  pid_t pid;

  printf("origin process pid : %d\n", getpid());

  pid = fork();
  /*- parent process : Child process의 PID
    - child process : 0*/

  if(pid == 0){
    /*child process*/
    printf("child process pid : %d\n", getpid());
  }
  else if (pid > 0){
    /*parent process*/
    printf("parent process pid : %d, child process pid : %d\n",getpid(), pid);
  }

  test_func();
  
  return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

static int append_file(void){
  int fd;

  fd = open("datafile", O_WRONLY | O_APPEND);
  // 있던 파일에 내용을 추가하니까 권한은 필요 없음.
  if(fd == -1){
    printf("open() error\n");
    return -1;
  }

  dprintf(fd, "hello again");

  close(fd);
  return 0;
}

static int trunc_fail(void){
  int fd;

  fd = open("datafile", O_WRONLY | O_CREAT | O_TRUNC , 0600);
  if (fd == -1){
    printf("open() error\n");
    return -1;
  }

  dprintf(fd, "byebye file\n");
  close(fd);
  return 0;
}

static int write_file(void){
  int fd;

  fd = open("datafile", O_WRONLY | O_CREAT, 0644);
  if(fd == -1){
    printf("open() error\n");
    return -1;
  }

  dprintf(fd, "hello world!! %d\n",123);

  close(fd);
  return 0;
}

int main(int argc, char **argv){
  if(write_file()){
    printf("write_file() error\n");
    return -1;
  }
  if(trunc_fail()){
    printf("trunc_file() error\n");
    return -1;
  }
  if(append_file()){
    printf("append_file() error\n");
    return -1;
  }
  return 0;
}
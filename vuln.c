#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  char buffer[8] = {0};
  printf("Please enter your name:");
  scanf("%s", buffer);
  return 0;
}
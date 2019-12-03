
int time(int);
void srand(unsigned int seed);
int rand(void);
unsigned int sleep(unsigned int seconds);
unsigned int read(int fd, void *buf, unsigned int count);
int strcmp(const char *s1, const char *s2);
int printf(const char *format, ...);

int main(int agrc, char *argv[], char *envp[]){

  char buff[10];

  int v = time(0);
  srand(v);
  int v2 = rand();
  sleep(v2);
 
  read(0, buff, 10); 
  buff[9] = '\0';
  if( ! strcmp(buff, "1337") )
    printf("%c%c%c%c{%c%c%c%c%c%c%c%c}\n", 'f', 'l', 'a', 'g', 'G','0','0','d','_','B','o','y');
  else 
    printf("Nothing for you here\n");
  return 0;
}

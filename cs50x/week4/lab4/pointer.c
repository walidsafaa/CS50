#include <stdio.h>

int main(void)
{
    int n = 50;
    int* ptr = NULL;
    ptr = &n;
    printf("%p\n", ptr);
}
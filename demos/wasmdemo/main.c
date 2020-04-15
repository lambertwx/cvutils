#include <stdio.h>

long long fib(int n) {
    if (n <= 1) return 1;
    printf("Computing fib %d", n);
    return fib(n - 1) + fib(n - 2);
}

int main() {
    printf("At beginning of main\n");
    printf("%lld\n", fib(11));
    printf("At end of main\n");
    return 0;
}


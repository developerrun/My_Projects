#include <stdio.h> 
#include <unistd.h> // Required header for getpid()
#include <stdlib.h>

// Run two instances of the code on two terminals, this proves how value is being overwritten continously as the execution proceeds.

int main(){
    
    
    int *p = malloc(sizeof(int));
    *p = 0;
    
    while(1){
        printf("(%d) p: address of p: %p | Value of p: %d", getpid(),(void*)p,*p); 
        *p = *p + 1;  
        fflush(stdout);
        sleep(1); 
    }
     
}

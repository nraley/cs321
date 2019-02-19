/*Function to capture still photos every 1 second*/

#include <stdio.h>
#include <unistd.h>

void photoCap();    //function prototype

int main() {
    while(1) {
        photoCap();
        sleep(1);
    }
    return 0;
}

void photoCap() {
    printf("Photo captured\n");
}

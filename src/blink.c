#include <signal.h>
#include <mraa/gpio.h>

sig_atomic_t volatile runf = 1;

void ISRS(int sig){
	if(sig == SIGINT)
		runf = 0;
}

int main(){

mraa_gpio_context ld;
ld = mraa_gpio_init(13);
mraa_gpio_dir(ld, MRAA_GPIO_OUT);

//signal(SIGINT, ISRS);

while(runf){
mraa_gpio_write(ld, 1);
sleep(1);
mraa_gpio_write(ld, 0);
sleep(1);
}
mraa_gpio_close(ld);
return 0;
}

 
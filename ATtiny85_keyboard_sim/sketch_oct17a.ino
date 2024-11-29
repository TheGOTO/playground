
https://github.com/adafruit/Adafruit-Trinket-USB

/*
TrinketKeyboard example
For Trinket by Adafruit Industries
*/

//#include <TrinketKeyboard.h>
#include <TrinketMouse.h>



void setup()
{
  

  // start USB stuff
  //TrinketKeyboard.begin();

  TrinketMouse.begin();
}


void sim_poll()
{

  // the poll function must be called at least once every 10 ms
  // or cause a keystroke
  // if it is not, then the computer may think that the device
  // has stopped working, and give errors
  //TrinketKeyboard.poll();

}

void sim_keyboard()
{
 
  


  //TrinketKeyboard.print("Hello World!");

  
  //TrinketKeyboard.pressKey(KEYCODE_MOD_LEFT_GUI, 0);
   // this releases the key (otherwise it is held down!)
  //TrinketKeyboard.pressKey(0, 0);
  delay(3000);


}

void sim_mous()
{
  
  


  TrinketMouse.move(500, 500, random(), 0x00); 

}


void loop()
{
 
  //sim_poll();
  //sim_keyboard();


  sim_mous();

}




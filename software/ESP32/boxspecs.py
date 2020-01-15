
class Boxspecs():
    def __init__():
        # output pins
        print("inclass")
        # hlPin = 13 # house light pin
        # ckPin = 3 # clicker pin
        # rw1Pin = 4 # reward pin
        # tnPin = 5 # tone  pin;
        # cl1Pin = 6 # cue light1 pin
        # cl2Pin = 7 # cue light2 pin
        # # input pins
        # hpPin = A0 #head port
        # lsPin = A1 #lick spout
        #
        # #set each port as input or output
        # led = machine.Pin(2, machine.Pin.OUT)
        # hl = machine.Pin(hlPin, machine.Pin.OUT)
        # ck = machine.Pin(ckPin, machine.Pin.OUT)
        # rw1 = machine.Pin(rw1Pin, machine.Pin.OUT)
        # cl1 = machine.Pin(cl1Pin, machine.Pin.OUT)
        # cl2 = machine.Pin(cl2Pin, machine.Pin.OUT)
        #
        # hp = machine.Pin(hpPin, machine.Pin.IN)
        # ls = machine.Pin(lsPin, machine.Pin.IN)





# variables to count time
timing1 =0
timing2 =0

trials = 10 # number of trials

# duration of events (in milliseconds)

itiDur = 1000 #ITI
rwDur = 100 #reward (the amount of time the pump stays on)
tnDur = 400 #tone
cl1Dur = 100 #cue1
cl2Dur = 200 #cue2
csDur = 200 #cs duration
csusDur = 500 #cs us interval

# variables for support functions
arraySize = 6
#outputPorts = [0,0,0,0,0,0]

#void setup() {
#// tell the board what are the "directions of each pin



void loop() {
  // put your main code here, to run repeatedly:

//iti
//set all outputs to off
digitalWrite(hlPin,LOW);
digitalWrite(ckPin,LOW);
digitalWrite(rw1Pin,LOW);
digitalWrite(tnPin,LOW);
digitalWrite(cl1Pin,LOW);
digitalWrite(cl2Pin,LOW);

//set all values of output array to 0 so that we don't turn anything on
//while ITI is going on.

outputPorts[0] = {0};
outputPorts[1] = {0};
outputPorts[2] = {0};
outputPorts[3] = {0};
outputPorts[4] = {0};
outputPorts[5] = {0};

//count time for this phase

timing(itiDur,outputPorts);
// the timing function above is declared after the void loop is finished

//CS+US
//decide which cue is going to be on
//cue light 1 example
outputPorts[0]=cl1Pin;
timing(csDur, outputPorts);

//timing(csusDur,0);

//start the US
//timing(rwDur, rw1Pin);



}//end void loop

/*
void setPorts(int outports){


  }//end setPorts
*/

void timing( int waitTime,int outputports){
  // since one set of commands are repeated a lot
  // in the main loop, this function generalises these
  // repetitions to make the code easier to read and debug

  // the code is doing the following:
  // 1 - turn  output ports high
  // 2 - count time and check the status of input ports
  // 3 - turn output port LOW



  // run throught the outputport array
  for (byte i = 0; i < arraySize; i++) {
      // only change a port setting if the port is not set to 0
      // port set to zero means that the function will just count a certain
      // amount of time and check input port states,
      // but it will not change port states
      if (outputPorts[i] ==0){
        digitalWrite(outputPorts[i], HIGH);
    }//end if
  }// end for loop

  //count time between US is given
  timing1 = millis();
  timing2 = millis();
  while (timing2-timing1 < waitTime){
    timing2 = millis();
    analogRead(hpPin);
    analogRead(lsPin);
  }//end US interval while loop

  for (byte i = 0; i < arraySize; i++) {
      // only change a port setting if the port is not set to 0
      // port set to zero means that the function will just count a certain
      // amount of time and check input port states,
      // but it will not change port states
      if (outputPorts[0] !=0){
        digitalWrite(outputPorts[i], LOW);
    }//end if
  }// end for loop


  }// end timing function

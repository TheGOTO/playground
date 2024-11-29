// usage
// <command>

const byte numChars = 32;
char receivedChars[numChars];
int pin_C=11;
int pin_D=12;
String status;

boolean newData = false;

void setup() {
    Serial.begin(9600);
    print_help();
    pinMode(pin_C, OUTPUT); // Setzt den Digitalpin als Outputpin
    pinMode(pin_D, OUTPUT); // Setzt den Digitalpin als Outputpin
    
    normal_mode();
    //max_mode();
}

void loop() {
    recvWithStartEndMarkers();
    showNewData();
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void print_help()
{
          Serial.println("Welcome to the Smart-Grid-Gateway v1");
          Serial.println("");
          
          Serial.print("C/K2 is configured as PIN ");
          Serial.println(pin_C);
          Serial.print("D/K1 is configured as PIN ");
          Serial.println(pin_D);
          
          Serial.println("");
          Serial.println("Commands: ");
          Serial.println("<normal-mode>");
          Serial.println("<evu-lock-mode>");
          Serial.println("<adapted-mode>");
          Serial.println("<max-mode>");
          Serial.println("<status>");
}

void normal_mode()
{
    digitalWrite(pin_C, HIGH); 
    digitalWrite(pin_D, HIGH); 
    status="normal-mode";
    Serial.println("normal-mode activated");  
}

void max_mode()
{
  digitalWrite(pin_C, LOW); 
  digitalWrite(pin_D, LOW); 
  status="max-mode";
  Serial.println("max-mode activated");
}

void get_status()
{
    //Serial.print("Current Mode: ");
    Serial.println(status);
    
}



void showNewData()
 {
    if (newData == true) 
    {
        String input(receivedChars);        
           
        if(input=="status")     
        {
          get_status();
        }
        else if(input=="normal-mode")     
        {
          normal_mode();
        }
        else if(input=="evu-lock-mode")
        {
          digitalWrite(pin_C, LOW);
          digitalWrite(pin_D, HIGH); 
          status="evu-lock-mode";
          Serial.println("evu-lock-mode activated");
        }
        else if(input=="adapted-mode")
        {
          digitalWrite(pin_C, HIGH); 
          digitalWrite(pin_D, LOW); 
          status="adapted-mode";
            Serial.println("adapted-mode activated");
        }
        else if(input=="max-mode")
        {
          max_mode();
        }
        else
        {
          print_help();

        }
        newData = false;
    }
}

void setup() {
  Serial.begin(9600); 
  pinMode(7,OUTPUT); 
  pinMode(8,OUTPUT);
  // put your setup code here, to run once:


}
int howlong; 
String full = "";
bool holding = false; 
bool shooting = false;
void shoot(){
  if(shooting){
  digitalWrite(7,HIGH); 
  digitalWrite(8,HIGH);
  delay(howlong);
  digitalWrite(7,LOW); 
  digitalWrite(8,LOW);
  delay(howlong); 
  }
  
}

void loop() {
   
  if(Serial.available() > 0){
    char a = Serial.read(); 
    if(a == 'v'){
      howlong = 108/3;
    }else if (a == 'p'){
      howlong = 91/5; 
    }else if (a == 's'){
      howlong = 75/5;
    }else if (a == 'u'){
      howlong = 109/5; 
    }else if (a == 'a'){
      howlong = 77/5;
    }else if (a == 'o'){
      howlong = 64/2;
    }else if (a == 'i'){
      howlong = 55/2;

    
    }else{
    full +=a; 
    }
    Serial.println(a); 
  



}

if(full.charAt(0) == 'e' && full.charAt(full.length()-1) == 'e' && full.length()>1){
    full = full.substring(1,full.length()-1); 
    
    if(full.toInt() == 1){
      shooting = true; 
    }else{
      shooting = false;
    }
    //Serial.println(full);
    full = "";
  }
    holding = true;
  
  shoot(); 

  // put your main code here, to run repeatedly:
}

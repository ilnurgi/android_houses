/*
 * 1. посекундно мигает
 * 2. и отпраялет по сериному порту время работы устройства
 */
 
// номер светового индикатора
int ledPin =  13;      

// пин фоторезитора, и значение фоторезистора
int photoPin = 2;
int photoValue = 0;

// функция, настройка окужения
void setup() {
  // пин у нас на выход
  pinMode(ledPin, OUTPUT); 
  pinMode(photoPin, INPUT); 
  Serial.begin(9600);  
}

// бесконечный цикл работы устройства
void loop()
{
  // включаем индикатор
  digitalWrite(ledPin, HIGH);
  
  // спим 500 мсек
  delay(500);
  
  // выключаем индикатор
  digitalWrite(ledPin, LOW);
  
  // спим 500 сек
  delay(500);
  
  // получаем время работы устройства, в миллисекундах
  // и отправялем данные по сериному порту, по USB
  photoValue = digitalRead(photoPin);
  Serial.println(photoValue);
}


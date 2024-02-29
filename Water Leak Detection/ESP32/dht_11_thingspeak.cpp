#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <WiFi.h>
#include <ThingSpeak.h>

#define DHTPIN 5     // Digital pin connected to the DHT sensor
#define DHTTYPE    DHT11     // DHT 11

DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;

// WiFi 정보와 ThingSpeak 채널 정보를 입력합니다.
const char* ssid     = "KSW Guest"; 
const char* password = "M1gukHappy15!"; 
unsigned long myChannelNumber = 2405093; 
const char * myWriteAPIKey = "24YMCSH6ZYMWSLR9"; 

WiFiClient  client;

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");

  ThingSpeak.begin(client);  // ThingSpeak 라이브러리를 시작합니다.

  dht.begin();
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  delayMS = sensor.min_delay / 1000;
}

void loop() {
  delay(delayMS);

  sensors_event_t event;
  dht.temperature().getEvent(&event);
  float temperature = event.temperature;
  
  dht.humidity().getEvent(&event);
  float humidity = event.relative_humidity;

  if (isnan(temperature)) {
    Serial.println(F("Error reading temperature!"));
  } else {
    Serial.print(F("Temperature: "));
    Serial.print(temperature);
    Serial.println(F("°C"));
    ThingSpeak.setField(1, temperature); // 1은 필드 번호입니다.
  }

  if (isnan(humidity)) {
    Serial.println(F("Error reading humidity!"));
  } else {
    Serial.print(F("Humidity: "));
    Serial.print(humidity);
    Serial.println(F("%"));
    ThingSpeak.setField(2, humidity); // 2는 필드 번호입니다.
  }

  // 모든 필드 업데이트를 ThingSpeak에 한 번에 전송합니다.
  int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  if(x == 200){
    Serial.println("Channel update successful.");
  } else {
    Serial.println("Problem updating channel. HTTP error code " + String(x));
  }

  delay(20000); // ThingSpeak는 15초 이내에 다시 데이터를 보낼 수 없으므로, 20초 간격으로 데이터를 전송합니다.
}

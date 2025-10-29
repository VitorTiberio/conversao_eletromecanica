// Projeto - Gerador CA + IoT // 

// Autor: Vitor Augusto Tibério - 14658834 - Engenharia Elétrica - EESC/USP 

// Incluindo as bibliotecas // 

#include <WiFi.h>
#include <WebServer.h>
#include <ESPAsyncWebServer.h>
#include <AsyncTCP.h>

// Configurando a rede // 

const char* ssid = "SEU_WIFI";
const char* password = "SENHA_WIFI";

// Definindo os pinos // 

#define TRIG 5
#define ECHO 18

// Canal WebSocket // 

AsyncWebServer server(80);
AsyncWebSocket ws("/ws");

// Definindo as funções // 

float getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn(ECHO, HIGH);
  distance = duration * 0.034 / 2;
  return distance;
}

void sendData() {
  float dist = getDistance();
  String msg = String(dist);
  ws.textAll(msg);
}

void setup() {
  Serial.begin(115200);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado! IP: " + WiFi.localIP().toString());

  ws.onEvent([](AsyncWebSocket *server, AsyncWebSocketClient *client, 
                 AwsEventType type, void *arg, uint8_t *data, size_t len) {});
  server.addHandler(&ws);

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", R"rawliteral(
      <!DOCTYPE html>
      <html>
      <head><meta charset="utf-8">
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script></head>
      <body>
        <h3>Distância (cm)</h3>
        <canvas id="chart"></canvas>
        <script>
          const ctx = document.getElementById('chart').getContext('2d');
          const chart = new Chart(ctx, {
            type: 'line',
            data: {labels: [], datasets: [{label: 'Distância', data: []}]},
            options: {scales: {y: {beginAtZero: true}}}
          });
          const ws = new WebSocket('ws://' + location.host + '/ws');
          ws.onmessage = e => {
            const val = parseFloat(e.data);
            chart.data.labels.push('');
            chart.data.datasets[0].data.push(val);
            if(chart.data.labels.length > 30){
              chart.data.labels.shift();
              chart.data.datasets[0].data.shift();
            }
            chart.update();
          };
        </script>
      </body></html>
    )rawliteral");
  });

  server.begin();
}

void loop() {
  sendData();
  delay(100); // envia a cada 100ms
}

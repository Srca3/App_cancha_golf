const int motorPin1 = 2;  // Pin del motor de la puerta 1
const int motorPin2 = 3;  // Pin del motor de la puerta 2

void setup() {
  Serial.begin(9600);
  
  // Inicializa los pines del motor como salidas
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  
  // Detiene ambos motores al inicio
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, HIGH);
}

void loop() {
  // Espera a recibir datos desde el Raspberry Pi
  if (Serial.available() > 0) {
    // Lee el valor de la puerta enviado desde el Raspberry Pi
    int puerta = Serial.parseInt();
    
    // Actúa según el valor de la puerta
    if (puerta == 0) {
      detenerMotores();
    } else if (puerta == 1) {
      abrirPuerta1();
    } else if (puerta == 2) {
      abrirPuerta2();
    }
    
    // Envia una confirmación al Raspberry Pi (opcional)
    Serial.println("Datos recibidos correctamente");
  }
}

void abrirPuerta1() {
  // Lógica para abrir la puerta 1
  digitalWrite(motorPin1, LOW);
  delay(2000);  // Ajusta el tiempo según sea necesario
  digitalWrite(motorPin1, HIGH);
}

void abrirPuerta2() {
  // Lógica para abrir la puerta 2
  digitalWrite(motorPin2, LOW);
  delay(2000);  // Ajusta el tiempo según sea necesario
  digitalWrite(motorPin2, HIGH);
}

void detenerMotores() {
  // Detiene ambos motores
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, HIGH);
}

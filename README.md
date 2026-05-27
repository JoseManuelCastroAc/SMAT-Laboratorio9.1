# Laboratorio 9.1 - SMAT IoT Telemetría

Sistema de monitoreo SMAT desarrollado con:

- FastAPI (Backend)
- Flutter (Aplicación móvil/escritorio)
- Python IoT Emulator
- SQLite

Este laboratorio simula sensores IoT que envían lecturas automáticas de nivel de agua hacia una API REST usando JWT y HTTP.

---

# Objetivo

Emular dispositivos IoT tipo ESP32/Raspberry Pi capaces de:

- Generar telemetría automáticamente
- Enviar datos cada pocos segundos
- Detectar niveles críticos
- Mostrar alertas visuales en la App Flutter
- Simular un sistema de monitoreo en tiempo real

---

# Estructura del Proyecto

```bash
PROYECTO_SMAT/
│
├── app/                 # Backend FastAPI
├── mobile/              # Aplicación Flutter
│
└── mobile/iot_device/   # Emulador IoT
```

---

# Requisitos

## Backend

```bash
pip install fastapi uvicorn sqlalchemy python-jose requests
```

## Flutter

- Flutter SDK instalado
- Visual Studio con Desktop Development

Verificar:

```bash
flutter doctor
```

## IoT

```bash
pip install requests
```

---

# Ejecución del Sistema Completo

El laboratorio utiliza 3 terminales simultáneamente.

---

# 1. Iniciar Backend FastAPI

Abrir terminal en la carpeta del backend:

```bash
cd PROYECTO_SMAT
```

Ejecutar:

```bash
uvicorn main:app --reload
```

o si el archivo está dentro de `/app`:

```bash
uvicorn app.main:app --reload
```

Debe aparecer:

```bash
Uvicorn running on http://127.0.0.1:8000
```

---

# 2. Ejecutar Flutter

Abrir terminal:

```bash
cd mobile
```

Ejecutar:

```bash
flutter clean
flutter pub get
flutter run -d windows
```

---

# 3. Ejecutar Emulador IoT

Abrir otra terminal:

```bash
cd mobile/iot_device
```

Ejecutar:

```bash
python sensor_emitter.py
```

---

# Funcionamiento del Emulador IoT

El script:

- Obtiene automáticamente el Token JWT
- Detecta todas las estaciones registradas
- Genera lecturas aleatorias
- Envía telemetría automáticamente
- Detecta niveles críticos

---

# Sistema de Alertas

Si el valor supera:

```text
70 cm
```

El sistema:

- Imprime alerta en consola
- Cambia color de la interfaz Flutter
- Simula modo de emergencia

---

# Flujo del Sistema

```text
IoT Emulator
      ↓
FastAPI Backend
      ↓
SQLite Database
      ↓
Flutter App
```

---

# Funcionalidades Implementadas

- Login JWT
- CRUD de estaciones
- Telemetría automática
- Alertas visuales
- Refresco automático
- Simulación multisensor
- Persistencia SQLite

---

# Prueba del Laboratorio

Para validar correctamente:

1. Crear estaciones desde Flutter
2. Ejecutar IoT
3. Verificar actualización automática
4. Confirmar alertas rojas cuando el valor > 70

---

# Autor

Victor Manuel Castro Acuña

Laboratorio 9.1 - Arquitectura IoT y Telemetría

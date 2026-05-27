# Laboratorio 9.1 - SMAT IoT Telemetría

Sistema de monitoreo SMAT desarrollado con:

- FastAPI (Backend)
- Flutter (Aplicación móvil/escritorio)
- Python IoT Emulator
- SQLite

---

# Objetivo

Emular dispositivos IoT tipo ESP32/Raspberry Pi capaces de:

- Generar telemetría automáticamente (Debajo del nombre, esta en verde)
- Enviar datos cada pocos segundos
- Detectar niveles críticos (Logica de negocio)

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

# Autor

Jose Manuel Castro Acuña

Laboratorio 9.1 - Arquitectura IoT y Telemetría

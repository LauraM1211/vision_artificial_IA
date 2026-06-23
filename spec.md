# Sistema de Visión Artificial para Detección y Conteo de Objetos

## 1. Descripción general

Aplicación web que utiliza técnicas de visión artificial para detectar y contar personas u objetos en tiempo real mediante una cámara web. El sistema procesará las imágenes capturadas por la cámara utilizando modelos de detección de objetos y mostrará los resultados en una interfaz web sencilla.

---

## 2. Objetivo

Desarrollar una aplicación basada en visión artificial capaz de identificar y contar personas u objetos en tiempo real, permitiendo automatizar procesos de monitoreo y control mediante el uso de una cámara web.

### Objetivos específicos

* Capturar video en tiempo real desde una cámara web.
* Detectar objetos mediante un modelo de inteligencia artificial.
* Contar automáticamente los objetos identificados.
* Mostrar los resultados en una interfaz web intuitiva.
* Facilitar la visualización de estadísticas básicas de detección.

---

## 3. Tecnologías

### Backend

* Python 3.11+
* FastAPI
* OpenCV
* Ultralytics YOLO
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript

### Herramientas de desarrollo

* Visual Studio Code
* Git
* GitHub

---

## 4. Arquitectura

El sistema seguirá una arquitectura cliente-servidor.

### Frontend

Responsable de:

* Mostrar la interfaz de usuario.
* Visualizar la cámara en tiempo real.
* Mostrar resultados de detección y conteo.

### Backend

Responsable de:

* Acceder a la cámara.
* Procesar imágenes mediante visión artificial.
* Detectar objetos utilizando YOLO.
* Enviar resultados al frontend mediante API REST.

### Flujo

1. Usuario accede al sistema.
2. Backend captura imágenes desde la cámara.
3. YOLO analiza cada fotograma.
4. Se detectan objetos y personas.
5. Se realiza el conteo.
6. Se envían los resultados al frontend.
7. El usuario visualiza las detecciones.

---

## 5. Módulos

### Módulo de Captura

Obtiene imágenes desde la cámara web.

### Módulo de Detección

Procesa las imágenes utilizando YOLO.

### Módulo de Conteo

Calcula la cantidad de objetos detectados.

### Módulo API

Expone endpoints para la comunicación con el frontend.

### Módulo de Interfaz

Muestra la información al usuario.

---

## 6. Entidades principales

### ObjetoDetectado

| Campo       | Tipo    |
| ----------- | ------- |
| id          | Integer |
| nombre      | String  |
| confianza   | Float   |
| coordenadas | Array   |

### Conteo

| Campo      | Tipo     |
| ---------- | -------- |
| categoria  | String   |
| cantidad   | Integer  |
| fecha_hora | DateTime |

---

## 7. Funcionalidades

### Funcionales

* Capturar video en tiempo real.
* Detectar personas.
* Detectar objetos.
* Mostrar recuadros sobre cada objeto detectado.
* Contar objetos automáticamente.
* Mostrar cantidad total detectada.
* Actualizar información en tiempo real.

### No funcionales

* Interfaz sencilla e intuitiva.
* Tiempo de respuesta rápido.
* Fácil mantenimiento del código.

---

## 8. Gestión de estado

### Backend

Mantendrá temporalmente:

* Objetos detectados.
* Conteo actual.
* Estado de la cámara.

### Frontend

Mantendrá:

* Conteo recibido del backend.
* Estado de conexión con la API.
* Visualización actual.

---

## 9. Reglas de negocio

1. Solo se contarán objetos con una confianza superior al 50%.
2. La cámara debe estar activa para iniciar detecciones.
3. Cada fotograma será procesado individualmente.
4. El conteo debe actualizarse en tiempo real.
5. El sistema debe evitar duplicar detecciones dentro del mismo fotograma.
6. Si no se detectan objetos, el contador mostrará cero.

---

## 10. Pantallas

### Pantalla Principal

Elementos:

* Vista de la cámara.
* Cantidad de objetos detectados.
* Estado del sistema.

### Pantalla de Resultados

Elementos:

* Total de objetos detectados.
* Categorías encontradas.
* Hora de la detección.

---

## 11. Navegación

```text
Inicio
│
├── Cámara en vivo
│
└── Resultados de detección
```

La navegación será simple debido al tamaño del proyecto.

---

## 12. Persistencia local

Se almacenará:

* Historial de detecciones.
* Cantidad de objetos detectados.
* Fecha y hora de cada detección.

Formato sugerido:

```json
{
  "fecha": "2026-06-18",
  "hora": "14:30",
  "objeto": "persona",
  "cantidad": 5
}
```

---

## 13. Criterios de aceptación

El proyecto será aceptado cuando:

* La cámara web funcione correctamente.
* El sistema detecte objetos en tiempo real.
* El conteo sea preciso.
* El frontend reciba datos del backend.
* La interfaz muestre los resultados correctamente.
* No existan errores críticos durante la ejecución.
* Se pueda realizar una demostración funcional completa.

---

## 14. Instrucciones para la IA

La IA deberá:

* Utilizar el modelo YOLO para detección de objetos.
* Procesar imágenes capturadas por OpenCV.
* Retornar resultados en formato JSON.
* Optimizar el rendimiento para tiempo real.
* Mantener código modular y documentado.
* Utilizar FastAPI para la exposición de servicios.

Ejemplo de respuesta:

```json
{
  "personas": 3,
  "objetos": 7,
  "estado": "activo"
}
```

---

## 15. Orden recomendado de implementación

### Fase 1

Configuración del entorno

* Crear proyecto.
* Crear entorno virtual.
* Instalar dependencias.

### Fase 2

Backend

* Configurar FastAPI.
* Configurar OpenCV.
* Integrar modelo YOLO.

### Fase 3

Detección

* Captura de cámara.
* Detección de objetos.
* Conteo automático.

### Fase 4

Frontend

* Crear interfaz HTML.
* Diseñar estilos CSS.
* Consumir API desde JavaScript.

### Fase 5

Integración

* Conectar frontend y backend.
* Mostrar resultados en tiempo real.

### Fase 6

Pruebas

* Validar detección.
* Validar conteo.
* Corregir errores.

### Fase 7

Entrega

* Documentación.
* README.
* Presentación final.

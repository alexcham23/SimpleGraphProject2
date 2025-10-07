# SimpleGraphProject2

## 📋 Descripción del Proyecto

SimpleGraphProject2 es una aplicación de escritorio desarrollada en Python que permite visualizar estructuras de datos mediante gráficos generados con Graphviz. El proyecto es capaz de procesar archivos con formato `.lfp` (Lenguajes Formales de Programación) que contienen definiciones de listas, matrices y tablas, y generar representaciones gráficas visuales de estas estructuras.

### Autor
- **Nombre:** Jaime Alejandro Armira Us
- **Carné:** 201602983
- **Curso:** Lenguajes Formales de Programación - Sección "A-"
- **Universidad:** Universidad de San Carlos de Guatemala

## ✨ Características Principales

- **Análisis Léxico y Sintáctico:** Procesamiento de archivos `.lfp` con sintaxis personalizada
- **Visualización de Estructuras de Datos:**
  - Listas enlazadas (simples y dobles)
  - Matrices bidimensionales
  - Tablas con encabezados
- **Generación de Gráficos:** Utiliza Graphviz para crear representaciones visuales
- **Personalización:** Soporte para diferentes colores y formas en los nodos
- **Reporte de Errores:** Generación de reportes HTML con errores léxicos y sintácticos
- **Interfaz Gráfica:** GUI intuitiva desarrollada con Tkinter

## 🎨 Tipos de Visualizaciones

### 1. Listas Enlazadas
- **Listas Simples:** Nodos conectados unidireccionalmente
- **Listas Dobles:** Nodos con enlaces bidireccionales

### 2. Matrices
- Representación visual de matrices con filas y columnas
- Personalización de colores y formas para cada elemento

### 3. Tablas
- Tablas con encabezados y contenido estructurado
- Formato HTML para visualización en navegador

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter:** Interfaz gráfica de usuario
- **Graphviz:** Generación de gráficos y diagramas
- **HTML/CSS:** Generación de reportes web

## 📦 Instalación

### Requisitos Previos

1. **Python 3.x** instalado en el sistema
2. **Graphviz** instalado y configurado en el PATH del sistema

### Instalación de Dependencias

```bash
# Instalar Graphviz (Windows)
# Descargar desde: https://graphviz.org/download/
# Agregar al PATH del sistema

# Instalar librería de Python para Graphviz
pip install graphviz
```

### Configuración del Proyecto

```bash
# Clonar el repositorio
git clone https://github.com/alexcham23/SimpleGraphProject2.git

# Navegar al directorio del proyecto
cd SimpleGraphProject2

# Ejecutar la aplicación
python main.py
```

## 🚀 Uso de la Aplicación

### Ejecución

```bash
python main.py
```

### Flujo de Trabajo

1. **Cargar Archivo:** Selecciona la opción 1 para cargar un archivo `.lfp`
2. **Generar Gráfica:** Selecciona la opción 2 para visualizar la gráfica generada
3. **Salir:** Selecciona la opción 3 para cerrar la aplicación

### Formato de Archivos .lfp

#### Ejemplo: Lista Enlazada

```
lista(
    defecto(
        nombre: 'Lista',
        forma: circulo,
        color: azul
    ),
    verdadero,
    nodos(
        nodo('A', azul2),
        nodo('B', rojo),
        nodo('C', verde)
    )
);
```

#### Ejemplo: Matriz

```
matriz(
    defecto(
        nombre: 'Matriz',
        forma: rectangulo,
        color: verde
    ),
    falso,
    fila(
        nodo('1', azul),
        nodo('2', rojo)
    ),
    fila(
        nodo('3', verde),
        nodo('4', amarillo)
    )
);
```

#### Ejemplo: Tabla

```
tabla(
    nombre: 'Tabla de Datos',
    encabezados(
        'ID', 'Nombre', 'Edad'
    ),
    fila('1', 'Juan', '25'),
    fila('2', 'María', '30')
);
```

## 🎨 Colores Disponibles

El sistema soporta los siguientes colores con tres variantes cada uno (color, color2, color3):

- Azul
- Rojo
- Amarillo
- Anaranjado
- Café
- Gris
- Morado
- Verde
- Blanco

## 🔷 Formas Disponibles

- Círculo
- Rectángulo
- Triángulo
- Punto
- Hexágono
- Diamante

## 📁 Estructura del Proyecto

```
SimpleGraphProject2/
│
├── main.py                 # Punto de entrada de la aplicación
├── Archivo.py              # Manejo de carga de archivos
├── analizadolista.py       # Analizador léxico/sintáctico para listas
├── analizadormatriz.py     # Analizador léxico/sintáctico para matrices
├── analizadortabla.py      # Analizador léxico/sintáctico para tablas
├── token.py                # Definición de tokens
├── lista.py                # Gestión de estructuras de datos y generación de gráficos
├── Graficar.py             # Módulo de generación de gráficos con Graphviz
├── HTML.py                 # Generación de reportes HTML
├── colorstart.py           # Mapeo de colores
├── figurasG.py             # Mapeo de formas geométricas
└── README.md               # Documentación del proyecto
```

## 🏗️ Arquitectura del Sistema

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                     CAPA DE PRESENTACIÓN                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              main.py (Tkinter GUI)                    │   │
│  │  - Ventana principal                                  │   │
│  │  - Menú de opciones                                   │   │
│  │  - Manejo de eventos                                  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   CAPA DE CONTROL DE FLUJO                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                  Archivo.py                           │   │
│  │  - Carga de archivos .lfp                            │   │
│  │  - Detección del tipo de estructura                  │   │
│  │  - Enrutamiento a analizadores específicos           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  CAPA DE ANÁLISIS LÉXICO                     │
│  ┌─────────────────┬──────────────────┬──────────────────┐  │
│  │ analizadolista  │ analizadormatriz │ analizadortabla  │  │
│  │                 │                  │                  │  │
│  │ - Análisis      │ - Análisis       │ - Análisis       │  │
│  │   léxico/       │   léxico/        │   léxico/        │  │
│  │   sintáctico    │   sintáctico     │   sintáctico     │  │
│  │ - Autómata      │ - Autómata       │ - Autómata       │  │
│  │   finito        │   finito         │   finito         │  │
│  └─────────────────┴──────────────────┴──────────────────┘  │
│                              ↓                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                     token.py                          │   │
│  │  - Identificación de tokens                          │   │
│  │  - Clasificación de lexemas                          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE GESTIÓN DE DATOS                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                     lista.py                          │   │
│  │  - Almacenamiento de nodos y estructuras             │   │
│  │  - Gestión de errores léxicos                        │   │
│  │  - Generación de código Graphviz                     │   │
│  │  - Funciones de limpieza y utilidad                  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  CAPA DE RENDERIZACIÓN                       │
│  ┌──────────────────┬───────────────────┬─────────────────┐ │
│  │   Graficar.py    │   colorstart.py   │   figurasG.py   │ │
│  │                  │                   │                 │ │
│  │ - Generación de  │ - Mapeo de        │ - Mapeo de      │ │
│  │   archivos .gv   │   colores a       │   formas a      │ │
│  │ - Renderización  │   códigos hex     │   Graphviz      │ │
│  │   PNG/SVG        │                   │                 │ │
│  └──────────────────┴───────────────────┴─────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE REPORTES                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    HTML.py                            │   │
│  │  - Generación de reportes de errores                 │   │
│  │  - Visualización de gráficos en navegador            │   │
│  │  - Formato HTML/CSS                                  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                     SALIDAS DEL SISTEMA                      │
│  ┌────────────────┬──────────────────┬───────────────────┐  │
│  │  Gráficos PNG  │  Archivos SVG    │  Reportes HTML    │  │
│  │  en Desktop    │  en Desktop      │  en directorio    │  │
│  └────────────────┴──────────────────┴───────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Descripción de Componentes

#### 1. Capa de Presentación
- **main.py:** Interfaz gráfica principal usando Tkinter
  - Ventana con menú de 3 opciones
  - Manejo de eventos de usuario
  - Coordinación del flujo de la aplicación

#### 2. Capa de Control de Flujo
- **Archivo.py:** Gestor de archivos de entrada
  - Diálogo para selección de archivos `.lfp`
  - Lectura de archivos con codificación UTF-8
  - Detección automática del tipo de estructura (lista/matriz/tabla)
  - Enrutamiento al analizador correspondiente

#### 3. Capa de Análisis Léxico/Sintáctico
- **analizadolista.py:** Analizador para listas enlazadas
- **analizadormatriz.py:** Analizador para matrices
- **analizadortabla.py:** Analizador para tablas

Cada analizador implementa:
- Autómata finito determinista (AFD)
- Funciones de estado (S0, S1, S2, ...)
- Validación sintáctica
- Captura de errores léxicos
- Construcción de estructuras de datos intermedias

- **token.py:** Clasificador de tokens
  - Identificación de palabras reservadas
  - Clasificación de operadores y símbolos
  - Reconocimiento de colores y formas

#### 4. Capa de Gestión de Datos
- **lista.py:** Gestión centralizada de datos
  - Listas de nodos y estados
  - Registro de errores léxicos
  - Funciones para generar código Graphviz
  - Utilidades de limpieza de datos

#### 5. Capa de Renderización
- **Graficar.py:** Motor de generación de gráficos
  - Creación de archivos `.gv` (Graphviz)
  - Renderización a PNG y SVG
  - Gestión de carpeta de salida
  
- **colorstart.py:** Conversión de colores a hexadecimal
- **figurasG.py:** Conversión de formas a sintaxis Graphviz

#### 6. Capa de Reportes
- **HTML.py:** Generador de reportes web
  - Creación de tablas HTML con errores
  - Inclusión de gráficos SVG
  - Apertura automática en navegador

### Flujo de Ejecución

1. **Usuario inicia la aplicación** → `main.py` muestra ventana
2. **Usuario selecciona "Cargar Archivo"** → `Archivo.py` abre diálogo
3. **Usuario elige archivo .lfp** → Se lee el contenido
4. **Sistema detecta tipo de estructura** → Enruta al analizador apropiado
5. **Analizador procesa el archivo** → Utiliza AFD para validar sintaxis
6. **Se construyen estructuras de datos** → Almacenadas en `lista.py`
7. **Sistema genera código Graphviz** → Código .gv creado
8. **Graphviz renderiza gráfico** → Archivos PNG/SVG generados
9. **Usuario selecciona "Generar Gráfica"** → `HTML.py` crea reporte
10. **Navegador muestra resultado** → Visualización completa

### Patrones de Diseño Utilizados

1. **Singleton Implícito:** Variables globales en `lista.py` para gestión centralizada de datos
2. **Strategy Pattern:** Diferentes analizadores para diferentes tipos de estructuras
3. **Factory Pattern:** Creación de nodos según tipo (lista/matriz/tabla)
4. **Template Method:** Estructura común en los tres analizadores con variaciones específicas

## 🔧 Manejo de Errores

El sistema implementa un robusto manejo de errores que incluye:

- **Detección de errores léxicos:** Caracteres no reconocidos
- **Detección de errores sintácticos:** Estructura incorrecta
- **Reporte detallado:** Fila, columna, carácter y descripción del error
- **Generación de tabla de errores:** Formato HTML con todos los errores encontrados

## 📊 Salida del Programa

Los archivos generados se almacenan en:
- **Windows:** `C:\Users\[usuario]\Desktop\projectGraphviz\`
  - Archivos `.gv` (código Graphviz)
  - Archivos `.png` (imagen del gráfico)
  - Archivos `.svg` (gráfico vectorial)

Los reportes HTML se generan en el directorio raíz del proyecto.

## 🔍 Funcionalidades Avanzadas

### Análisis Léxico
- Implementación de autómatas finitos deterministas
- Transiciones de estado documentadas
- Reconocimiento de múltiples tipos de tokens

### Personalización Visual
- 36 colores diferentes (12 colores × 3 variantes)
- 6 formas geométricas distintas
- Configuración de nodos por defecto
- Configuración de nodos individuales

### Generación de Gráficos
- Listas con enlace simple o doble
- Matrices con agrupación visual
- Tablas con formato HTML dentro de Graphviz

## 🐛 Solución de Problemas

### Graphviz no se encuentra
```bash
# Asegúrate de que Graphviz esté en el PATH
# Windows: Agregar C:\Program Files\Graphviz\bin al PATH
```

### Error al abrir archivos
```bash
# Verifica que el archivo tenga extensión .lfp
# Verifica que el formato sea correcto
```

### Errores de sintaxis
- Revisa que las palabras reservadas estén en minúsculas
- Verifica que todos los paréntesis y llaves estén balanceados
- Asegúrate de que cada instrucción termine con punto y coma

## 📝 Notas de Desarrollo

- El proyecto utiliza convenciones de nombres en español debido al contexto académico
- Los analizadores implementan máquinas de estados para el análisis léxico
- La arquitectura permite fácil extensión para nuevos tipos de estructuras

## 🤝 Contribuciones

Este es un proyecto académico. Para contribuciones o mejoras, por favor contacta al autor.

## 📄 Licencia

Proyecto académico desarrollado para el curso de Lenguajes Formales de Programación.

---

**Desarrollado con ❤️ en Guatemala**

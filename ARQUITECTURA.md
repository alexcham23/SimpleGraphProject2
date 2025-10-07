# Arquitectura del Sistema - SimpleGraphProject2

## 📐 Visión General de la Arquitectura

SimpleGraphProject2 implementa una arquitectura por capas (Layered Architecture) con separación clara de responsabilidades. El sistema está diseñado para procesar archivos de entrada, realizar análisis léxico y sintáctico, y generar visualizaciones gráficas de estructuras de datos.

## 🏛️ Arquitectura en Capas

### Capa 1: Presentación (Presentation Layer)

**Responsabilidad:** Interacción con el usuario

**Componentes:**
- `main.py`

**Funciones principales:**
```python
def winprin()      # Ventana principal
def ventanad()     # Ventana secundaria de opciones
def imprimr(event) # Manejador de eventos
def callback()     # Procesamiento de selección de menú
```

**Características:**
- Interfaz gráfica con Tkinter
- Menú interactivo con 3 opciones
- Gestión de ventanas y eventos
- Ciclo de vida de la aplicación

**Flujo de interacción:**
1. Inicialización de ventana principal
2. Espera de entrada del usuario
3. Procesamiento de selección
4. Invocación de servicios de capas inferiores
5. Reinicio del ciclo

---

### Capa 2: Control de Flujo (Application Layer)

**Responsabilidad:** Coordinación y enrutamiento

**Componentes:**
- `Archivo.py`

**Funciones principales:**
```python
def lectura()  # Carga de archivos y enrutamiento
```

**Características:**
- Diálogo de selección de archivos
- Lectura con codificación UTF-8
- Detección automática del tipo de estructura
- Enrutamiento inteligente a analizadores

**Lógica de enrutamiento:**
```python
if 'lista' in info.lower():
    analizador(info)       # → analizadolista.py
elif 'matriz' in info.lower():
    analizadorMatriz(info) # → analizadormatriz.py
elif 'tabla' in info.lower():
    analizadorTabla(info)  # → analizadortabla.py
```

---

### Capa 3: Análisis Léxico y Sintáctico (Business Logic Layer)

**Responsabilidad:** Procesamiento y validación de entrada

#### 3.1 Analizador de Listas (`analizadolista.py`)

**Autómata Finito Determinista (AFD):**

```
Estado 0 (S0): Estado inicial
  ↓ 'l' → Estado 1
  
Estado 1 (S1): Lectura de "lista"
  ↓ 'i' → Estado 2
  
Estado 2 (S2): Confirmación de palabra reservada
  ↓ 's' → Estado 3
  
Estado 3 (S3): Espera de '('
  ↓ '(' → Estado 4
  
Estado 4 (S4): Procesamiento de contenido
  ↓ 'd' → Estado 5 (defecto)
  ↓ 'n' → Estado 11 (nodos)
  
Estado 5 (S5): Análisis de sección "defecto"
  → Captura: nombre, forma, color
  
Estado 11 (S11): Análisis de nodos
  → Captura: contenido de nodos
  
Estado Final: Validación exitosa
```

**Variables globales:**
```python
numero = 1              # Contador de nodos
estado = 0              # Estado actual del autómata
fila = 1                # Línea actual
columna = 0             # Columna actual
errorcount = 0          # Contador de errores
nombredefect = ""       # Nombre por defecto
colordefect = ""        # Color por defecto
tipofigura = ""         # Forma por defecto
tipolista = ""          # Tipo de lista (simple/doble)
```

**Funciones de estado:**
- `S0` a `S23`: Cada función representa un estado del AFD
- `switch(concatenada)`: Dispatcher de estados
- `analizador(texto)`: Función principal de análisis

#### 3.2 Analizador de Matrices (`analizadormatriz.py`)

**Estructura similar a listas con diferencias:**

```python
matriz = []             # Matriz de nodos
auxlista = []           # Lista auxiliar para construcción
auxfilacount = 0        # Contador de filas
auxcolcount = 0         # Contador de columnas
filamatriz = 0          # Fila actual en matriz
columnamatriz = 0       # Columna actual en matriz
```

**Proceso de construcción de matriz:**
1. Lectura de configuración por defecto
2. Procesamiento fila por fila
3. Construcción de matriz bidimensional
4. Validación de dimensiones consistentes

#### 3.3 Analizador de Tablas (`analizadortabla.py`)

**Características especiales:**
- Manejo de encabezados
- Estructura de tabla HTML
- Validación de filas con mismo número de columnas

#### 3.4 Clasificador de Tokens (`token.py`)

**Tipos de tokens soportados:**

| Token | Descripción | Ejemplo |
|-------|-------------|---------|
| `Tk_lista` | Palabra reservada lista | `lista` |
| `Tk_matriz` | Palabra reservada matriz | `matriz` |
| `Tk_tabla` | Palabra reservada tabla | `tabla` |
| `Tk_fila` | Palabra reservada fila | `fila` |
| `Tk_nodo` | Palabra reservada nodo | `nodo` |
| `Tk_nodos` | Palabra reservada nodos | `nodos` |
| `Tk_defecto` | Palabra reservada defecto | `defecto` |
| `Tk_encabezado` | Palabra reservada encabezados | `encabezados` |
| `Tk_Numero` | Dígitos | `123` |
| `Tk_Cadena` | Texto entre comillas | `'texto'` |
| `Tk_color` | Color válido | `azul`, `rojo2` |
| `Tk_Forma` | Forma geométrica | `circulo`, `rectangulo` |
| `Tk_listaDobleEnlazada` | Boolean verdadero | `verdadero` |
| `Tk_listaSimple` | Boolean falso | `falso` |
| `Tk_Apertura_Parentesis` | Símbolo ( | `(` |
| `Tk_Cierre_Parentesis` | Símbolo ) | `)` |
| `Tk_Apertura_Llave` | Símbolo { | `{` |
| `Tk_Cierre_Llave` | Símbolo } | `}` |
| `Tk_coma` | Símbolo , | `,` |
| `Tk_Punto&coma` | Símbolo ; | `;` |
| `Desconocido` | Token no reconocido | - |

---

### Capa 4: Gestión de Datos (Data Management Layer)

**Responsabilidad:** Almacenamiento y organización de datos intermedios

**Componentes:**
- `lista.py`

**Estructuras de datos globales:**

```python
error = []           # Lista de errores léxicos
                    # Formato: [fila, columna, caracter, descripción]

evalue = []          # Lista de tokens válidos
                    # Formato: [fila, columna, lexema, token]

listaestados = []    # Lista de nodos/estados
                    # Formato: [encabezado, color]

tipo = 0            # Tipo de estructura (1=lista, 2=matriz, 3=tabla)
name = ""           # Nombre de la estructura
namedefect = ""     # Nombre por defecto
Colordefect = ""    # Color por defecto
figuradefect = ""   # Forma por defecto
tipolist = ""       # Tipo de lista (simple/doble)
```

**Funciones principales:**

```python
def limpiarlistas()
    # Limpia todas las estructuras de datos
    # Se llama al inicio de cada análisis

def llamar()
    # Carga configuración desde analizadolista
    # Procesa valores por defecto

def llamar2()
    # Carga configuración desde analizadormatriz
    # Similar a llamar() pero para matrices

def listaerror(fila, columna, caracter, descripcion)
    # Registra un error léxico
    # Agrega a la lista global de errores

def listavalue(fila, columna, lexema, token)
    # Registra un token válido
    # Agrega a la lista global de tokens

def estados(encabezado, color)
    # Registra un nodo/estado
    # Agrega a la lista global de estados

def graficarlist()
    # Genera código Graphviz para listas
    # Retorna string con código .gv

def graficarmatriz()
    # Genera código Graphviz para matrices
    # Crea nodos agrupados por columnas

def graficartabla()
    # Genera código Graphviz para tablas
    # Utiliza formato HTML dentro de Graphviz
```

---

### Capa 5: Renderización (Rendering Layer)

**Responsabilidad:** Generación de visualizaciones gráficas

#### 5.1 Motor de Gráficos (`Graficar.py`)

**Funciones principales:**

```python
def guardar()
    # Crea carpeta en Desktop si no existe
    # Ruta: C:\Users\[usuario]\Desktop\projectGraphviz\

def Grafico(graphi, name)
    # Genera archivo .gv con código Graphviz
    # Renderiza a PNG (con visualización)
    # Renderiza a SVG (sin visualización)
    # Elimina archivos anteriores si existen
```

**Proceso de renderización:**
1. Validación de carpeta de destino
2. Eliminación de archivos previos (si existen)
3. Creación de objeto Source con código Graphviz
4. Renderización a formato PNG (abre automáticamente)
5. Renderización a formato SVG (guardado silencioso)

#### 5.2 Mapeo de Colores (`colorstart.py`)

**Función:**
```python
def colorfill(cols)
    # Convierte nombre de color a código hexadecimal
    # Ejemplo: "azul" → "#2171b5"
```

**Paleta de colores:**

| Color Base | Variante 1 | Variante 2 | Variante 3 |
|------------|------------|------------|------------|
| Azul | #2171b5 | #08519c | #08306b |
| Rojo | #fee0d2 | #fc9272 | #de2d26 |
| Amarillo | #ffff99 | #ffff33 | #ffff00 |
| Anaranjado | #fee8c8 | #fdbb84 | #e34e33 |
| Café | #e08214 | #b35806 | #7f3b08 |
| Morado | #8073ac | #542788 | #2d004b |
| Gris | #dbdbdb | #969696 | #636363 |
| Verde | #238b45 | #006d2c | #00441b |
| Blanco | #ffffff | - | - |

#### 5.3 Mapeo de Formas (`figurasG.py`)

**Función:**
```python
def formG(dato)
    # Convierte nombre de forma a sintaxis Graphviz
```

**Mapeo de formas:**

| Entrada | Salida Graphviz |
|---------|----------------|
| circulo | circle |
| rectangulo | box |
| triangulo | triangle |
| punto | point |
| hexagono | hexagon |
| diamante | diamond |

---

### Capa 6: Reportes (Report Layer)

**Responsabilidad:** Generación de reportes HTML

**Componentes:**
- `HTML.py`

**Funciones principales:**

```python
def pageweb()
    # Genera reporte HTML completo
    # Incluye tabla de errores o visualización de gráfico
    # Abre automáticamente en navegador Chrome
```

**Estructura del reporte HTML:**

```html
<html>
  <head>
    <style>
      /* Estilos CSS para tablas */
    </style>
  </head>
  <body>
    <center>
      <!-- Si hay errores -->
      <table>
        <tr>
          <th>No.</th>
          <th>Fila</th>
          <th>Columna</th>
          <th>Caracter</th>
          <th>Descripción</th>
        </tr>
        <!-- Filas de errores -->
      </table>
      
      <!-- Si no hay errores -->
      <h2>Gráfica generada</h2>
      <img src="[ruta al SVG]"/>
    </center>
  </body>
</html>
```

---

## 🔄 Flujo de Datos Completo

### Caso de Uso: Cargar y Visualizar Lista

```
1. USUARIO → Ejecuta main.py
   ↓
2. MAIN.PY → Muestra ventana con menú
   ↓
3. USUARIO → Selecciona opción 1 (Cargar Archivo)
   ↓
4. ARCHIVO.PY → Abre diálogo de archivos
   ↓
5. USUARIO → Selecciona archivo.lfp
   ↓
6. ARCHIVO.PY → Lee contenido del archivo
   ↓ (detecta "lista")
7. ANALIZADOLISTA.PY → Inicia análisis léxico
   ↓
8. TOKEN.PY → Clasifica cada lexema
   ↓
9. ANALIZADOLISTA.PY → Valida sintaxis con AFD
   ↓ (si válido)
10. LISTA.PY → Almacena nodos y configuración
    ↓
11. USUARIO → Selecciona opción 2 (Generar Gráfica)
    ↓
12. HTML.PY → Verifica errores
    ↓ (si no hay errores)
13. LISTA.PY → graficarlist() genera código .gv
    ↓
14. COLORSTART.PY → Convierte colores a hex
    ↓
15. FIGURASG.PY → Convierte formas a Graphviz
    ↓
16. GRAFICAR.PY → Renderiza con Graphviz
    ↓
17. SISTEMA → Genera .png y .svg en Desktop
    ↓
18. HTML.PY → Genera reporte HTML
    ↓
19. NAVEGADOR → Muestra resultado final
    ↓
20. MAIN.PY → Reinicia ventana principal
```

---

## 🎯 Patrones de Diseño Implementados

### 1. Strategy Pattern (Patrón Estrategia)

**Ubicación:** Sistema de analizadores

**Implementación:**
- Interfaz común: Función analizador con parámetro texto
- Estrategias concretas:
  - `analizadolista.analizador()`
  - `analizadormatriz.analizadorMatriz()`
  - `analizadortabla.analizadorTabla()`

**Ventaja:** Permite cambiar dinámicamente el algoritmo de análisis según el tipo de estructura detectada.

### 2. Singleton Pattern (Patrón Singleton Implícito)

**Ubicación:** `lista.py`

**Implementación:**
- Variables globales compartidas
- Funciones de acceso centralizadas
- Estado único del sistema

**Ventaja:** Garantiza un único punto de acceso a los datos de la aplicación.

### 3. Template Method Pattern (Patrón Método Plantilla)

**Ubicación:** Analizadores léxicos

**Implementación:**
```python
# Estructura común en todos los analizadores
def analizador(texto):
    # 1. Inicialización
    inicializar_variables()
    limpiar_listas()
    
    # 2. Procesamiento (varía según tipo)
    while i < len(texto):
        procesar_caracter()
        switch(estado)
    
    # 3. Finalización
    if hay_errores():
        mostrar_errores()
    else:
        generar_grafico()
```

**Ventaja:** Define el esqueleto del algoritmo permitiendo que las subclases redefinan ciertos pasos.

### 4. Factory Method Pattern (Patrón Método Fábrica)

**Ubicación:** Funciones de creación de nodos

**Implementación:**
```python
def estados(encabezado, color):
    # Crea nodo según tipo de estructura
    lista = [encabezado, color]
    listaestados.append(lista)
```

**Ventaja:** Encapsula la creación de objetos sin especificar sus clases concretas.

### 5. State Pattern (Patrón Estado)

**Ubicación:** Autómatas finitos en analizadores

**Implementación:**
```python
# Cada estado es una función
def S0(concatenada): # Estado 0
    if concatenada == 'l':
        estado = 1
        
def S1(concatenada): # Estado 1
    if concatenada == 'i':
        estado = 2
        
# Dispatcher
def switch(concatenada):
    if estado == 0:
        S0(concatenada)
    elif estado == 1:
        S1(concatenada)
```

**Ventaja:** Permite que un objeto altere su comportamiento cuando su estado interno cambia.

---

## 🧩 Dependencias del Sistema

### Dependencias Externas

```
Python 3.x
  ├── tkinter (GUI)
  │   ├── tk (ventanas)
  │   ├── filedialog (selección de archivos)
  │   └── messagebox (mensajes)
  │
  ├── graphviz (generación de gráficos)
  │   ├── Digraph
  │   ├── Source
  │   └── render
  │
  ├── webbrowser (apertura de HTML)
  ├── os (gestión de archivos)
  └── sys (control del sistema)
```

### Dependencias Internas

```
main.py
  └── Archivo.py
        ├── analizadolista.py
        │     ├── token.py
        │     └── lista.py
        │           ├── Graficar.py
        │           ├── colorstart.py
        │           └── figurasG.py
        │
        ├── analizadormatriz.py
        │     ├── token.py
        │     └── lista.py
        │
        └── analizadortabla.py
              ├── token.py
              └── lista.py

main.py
  └── HTML.py
        └── lista.py
```

---

## 🔐 Consideraciones de Seguridad

1. **Validación de Entrada:**
   - Verificación de extensión de archivo (.lfp)
   - Análisis léxico exhaustivo
   - Detección de caracteres inválidos

2. **Manejo de Errores:**
   - Try-catch implícito en lecturas de archivo
   - Validación de estados del autómata
   - Mensajes de error descriptivos

3. **Gestión de Recursos:**
   - Cierre apropiado de archivos
   - Limpieza de variables globales
   - Eliminación de archivos temporales

---

## 📈 Escalabilidad y Extensibilidad

### Para Agregar un Nuevo Tipo de Estructura:

1. **Crear nuevo analizador:**
   ```python
   # analizadorgrafo.py
   def analizadorGrafo(texto):
       # Implementar AFD
       # Llamar a token.py
       # Almacenar en lista.py
   ```

2. **Actualizar enrutador:**
   ```python
   # Archivo.py
   elif 'grafo' in info.lower():
       analizadorGrafo(info)
   ```

3. **Agregar función de graficación:**
   ```python
   # lista.py
   def graficargrafo():
       # Generar código Graphviz
       # Llamar a Grafico()
   ```

4. **Actualizar tokens si necesario:**
   ```python
   # token.py
   elif dato.lower()=="grafo":
       tipo="Tk_grafo"
   ```

### Mejoras Potenciales:

1. **Capa de Persistencia:**
   - Base de datos para almacenar historial
   - Caché de gráficos generados

2. **API REST:**
   - Exponer funcionalidad vía web
   - Procesamiento asíncrono

3. **Validación Avanzada:**
   - Análisis semántico
   - Optimización de gráficos

4. **Exportación Múltiple:**
   - PDF, JPEG, GIF
   - Diferentes estilos de gráficos

---

## 🧪 Testing y Validación

### Tipos de Pruebas Recomendadas:

1. **Pruebas Unitarias:**
   - Función tokens() con diferentes entradas
   - Funciones colorfill() y formG()
   - Funciones de estado (S0, S1, etc.)

2. **Pruebas de Integración:**
   - Flujo completo de carga → análisis → graficación
   - Interacción entre analizadores y lista.py

3. **Pruebas de Sistema:**
   - Interfaz gráfica completa
   - Generación de archivos
   - Apertura de navegador

4. **Pruebas de Aceptación:**
   - Casos de uso reales
   - Validación con diferentes archivos .lfp

### Casos de Prueba Críticos:

| Caso | Entrada | Resultado Esperado |
|------|---------|-------------------|
| Lista válida | lista.lfp | Gráfico PNG/SVG |
| Matriz válida | matriz.lfp | Gráfico PNG/SVG |
| Tabla válida | tabla.lfp | Gráfico PNG/SVG |
| Error léxico | archivo con caracteres inválidos | Reporte de errores |
| Error sintáctico | paréntesis no balanceados | Mensaje de error |
| Archivo vacío | archivo.lfp vacío | Mensaje de error |
| Colores inválidos | nodo con color desconocido | Error o color por defecto |

---

## 📚 Referencias Técnicas

### Conceptos Utilizados:

1. **Autómatas Finitos Deterministas (AFD)**
   - Teoría de lenguajes formales
   - Máquinas de estado

2. **Análisis Léxico y Sintáctico**
   - Compiladores
   - Procesamiento de lenguajes

3. **Graphviz DOT Language**
   - Lenguaje de descripción de gráficos
   - Sintaxis y semántica

4. **Patrones de Diseño**
   - Gang of Four (GoF)
   - Arquitecturas de software

---

## 🔄 Ciclo de Vida del Desarrollo

### Fase 1: Análisis
- Definición de gramática del lenguaje .lfp
- Diseño de autómatas finitos
- Especificación de tokens

### Fase 2: Diseño
- Arquitectura por capas
- Definición de interfaces
- Diseño de estructuras de datos

### Fase 3: Implementación
- Desarrollo de analizadores léxicos
- Implementación de generadores de gráficos
- Creación de interfaz gráfica

### Fase 4: Pruebas
- Validación con archivos de ejemplo
- Corrección de errores
- Optimización de rendimiento

### Fase 5: Despliegue
- Documentación completa
- Instalación de dependencias
- Capacitación de usuarios

---

## 💡 Lecciones Aprendidas y Mejores Prácticas

1. **Separación de Responsabilidades:**
   - Cada módulo tiene una función clara
   - Facilita mantenimiento y debugging

2. **Variables Globales Controladas:**
   - Uso centralizado en lista.py
   - Funciones de limpieza consistentes

3. **Análisis Incremental:**
   - Procesamiento carácter por carácter
   - Detección temprana de errores

4. **Generación Modular de Código:**
   - Construcción por partes del código Graphviz
   - Facilita modificaciones y extensiones

5. **Interfaz Usuario-Amigable:**
   - Mensajes claros de error
   - Visualización automática de resultados
   - Flujo intuitivo de trabajo

---

**Documento preparado para:** Proyecto #2 - Lenguajes Formales de Programación  
**Autor:** Jaime Alejandro Armira Us - 201602983  
**Fecha:** 2024  
**Versión:** 1.0

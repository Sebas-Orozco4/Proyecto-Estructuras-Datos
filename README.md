
# PROYECTO DE ESTRUCTURAS DE DATOS LINEALES

## Sistema de Gestión de Despacho de Pedidos en una Bodega

### 1. Integrantes

- Sebastián Orozco Duque - Número de lista: 13
- Miguel Ángel Sepúlveda - Número de lista: 21

### 2. Objetivo

Desarrollar un simulador de despacho de pedidos aplicando estructuras de datos lineales, específicamente colas, y resolver ejercicios de programación relacionados con pilas y colas.

### 3. Tecnología utilizada

- Lenguaje: Python 3
- Editor: Visual Studio Code
- Plataforma de ejercicios: LeetCode
- Control de versiones: Git y GitHub

### 4. Cálculo de capacidad máxima

Los integrantes se organizan alfabéticamente por apellido:

1. Orozco: Sebastián - Número de lista 13.
2. Sepúlveda: Miguel Ángel - Número de lista 21.

N = 13

Fórmula:

capacidadMax = (N % 4) + 3

capacidadMax = (13 % 4) + 3

capacidadMax = 1 + 3

capacidadMax = 4

La capacidad máxima del simulador es de 4 pedidos.

### 5. Descripción del simulador

El sistema representa una bodega que registra y despacha pedidos.

Se utiliza una estructura de datos Cola (Queue), que funciona bajo el principio FIFO (First In, First Out): el primer pedido que ingresa es el primero que sale.

Funciones del simulador:

- Registrar pedidos.
- Despachar pedidos.
- Consultar el siguiente pedido.
- Mostrar pedidos pendientes.
- Controlar la capacidad máxima.
- Generar mensajes de Overflow y Underflow.

La cola se implementa mediante nodos enlazados.

### 6. Análisis de complejidad del simulador

| Operación | Complejidad temporal |
|---|---|
| Agregar pedido | O(1) |
| Despachar pedido | O(1) |
| Consultar siguiente pedido | O(1) |
| Mostrar pedidos | O(n) |

Complejidad espacial: O(n), debido al almacenamiento de los nodos de los pedidos.

### 7. Ejercicios de LeetCode

#### Ejercicio 1: Valid Parentheses

- Número: 20.
- Dificultad: Easy.
- Estructura: Stack (Pila).
- Complejidad temporal: O(n).
- Complejidad espacial: O(n).

La solución utiliza una pila para comprobar que los símbolos de apertura y cierre estén correctamente organizados.

#### Ejercicio 2: Implement Queue using Stacks

- Estructura: dos pilas.
- Dificultad: Easy.
- Complejidad temporal:
  - Push: O(1).
  - Pop: O(1) amortizado.
  - Peek: O(1) amortizado.
  - Empty: O(1).
- Complejidad espacial: O(n).

La solución utiliza dos pilas para simular el comportamiento FIFO de una cola.

### 8. Evidencias

Se incluyen evidencias del funcionamiento del simulador y de los ejercicios de LeetCode:

- Resultados Accepted de los dos ejercicios.
- Registro de cuatro pedidos.
- Mensaje Overflow al intentar agregar un quinto pedido.
- Despacho de pedidos siguiendo el orden FIFO.
- Mensaje Underflow al intentar despachar cuando la cola está vacía.

### 9. Conclusión

El proyecto permitió aplicar estructuras de datos lineales en un escenario práctico de despacho de pedidos.

Se implementó una cola mediante nodos enlazados, se estableció una capacidad máxima y se analizaron las complejidades temporales y espaciales de sus operaciones.

También se aplicaron los conocimientos de pilas y colas mediante ejercicios de programación en LeetCode.

# Bomberman
## Listas enlazadas - 2024-1
El objetivo de esta práctica es diseñar e implementar una versión básica del juego Bomberman, utilizando exclusivamente listas enlazadas para gestionar el mapa del juego, el jugador principal, los enemigos, y los obstáculos. Esta versión simplificada del juego debe permitir al jugador moverse, colocar bombas, destruir obstáculos, eliminar enemigos, y recoger habilidades para aumentar su capacidad de destrucción y supervivencia.

### Descripción del Problema:
En el juego Bomberman, el jugador principal debe navegar por un mapa lleno de obstáculos destructibles y enemigos que se mueven aleatoriamente. El jugador puede colocar bombas para destruir obstáculos y eliminar enemigos, buscando sobrevivir y eventualmente eliminar a todos los enemigos del mapa para ganar.

### Requisitos de la Implementación:
* *Mapa del Juego*: El mapa debe ser representado como una matriz enlazada de NxN, donde cada celda puede contener:
  * Espacio vacío.
  * Un bloqueo (obstáculo destructible).
  * El jugador principal.
  * Un enemigo.
  * Una bomba.
  * Una habilidad (aumentar el número de bombas o el rango de las bombas).

* *Jugador Principal*: El jugador debe poder moverse en direcciones verticales y horizontales. Inicialmente, el jugador puede colocar una bomba a la vez, con un rango de destrucción de una celda en todas direcciones. 

* *Bombas y Explosiones*: Las bombas tienen un tiempo de detonación predefinido (ustedes lo definen). Al explotar, afectan las celdas adyacentes dentro de su rango. El rango puede aumentarse recogiendo habilidades específicas. Las bombas no afectan al jugador principal.

* *Enemigos*: Debe haber N enemigos en el mapa que se mueven aleatoriamente en direcciones verticales u horizontales. Si un enemigo alcanza la celda del jugador principal, el jugador pierde.

* *Habilidades*: Las habilidades para recoger incluyen aumentar la cantidad máxima de bombas que el jugador puede colocar simultáneamente y aumentar el rango de destrucción de las bombas.

* *Restricción de Estructuras de Datos*: El uso de matrices bidimensionales tradicionales, listas dinámicas predefinidas, y otras estructuras de datos auxiliares está estrictamente prohibido. Toda la representación del mapa y las entidades del juego deben basarse en listas enlazadas y objetos. Defina las clases y tipos de listas enlazadas que considere necesarias. 

* *Fin del Juego*: El juego termina cuando todos los enemigos han sido eliminados (victoria) o cuando el jugador es alcanzado por un enemigo (derrota).
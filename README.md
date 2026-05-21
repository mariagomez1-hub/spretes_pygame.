# Sprites, grupos y programación orientada a objetos en Pygame

## Introducción

En Pygame, los sprites son objetos gráficos utilizados para representar personajes, enemigos, objetos y elementos visuales de un videojuego.  
Cada sprite posee una imagen, una posición y comportamientos propios.

El uso de grupos (`Group`) permite administrar múltiples sprites de manera eficiente, facilitando:
- actualización de objetos,
- dibujo en pantalla,
- detección de colisiones,
- organización del código.

## Conceptos principales
### Sprite
Un sprite es un objeto gráfico que combina:
- imagen,
- posición,
- propiedades,
- comportamiento.

### Group
Un grupo es una colección de sprites.

Permite:
- actualizar varios sprites simultáneamente,
- dibujarlos en pantalla,
- administrar colisiones.

### Programación orientada a objetos
Pygame utiliza clases y objetos.

Conceptos importantes:
- Clase
- Objeto
- Herencia
- Métodos
- Atributos
- Constructor (__init__)

### Método update()
El método `update()` se ejecuta automáticamente para actualizar el comportamiento del sprite.

### Colisiones
Las colisiones permiten detectar cuando dos objetos gráficos se tocan.
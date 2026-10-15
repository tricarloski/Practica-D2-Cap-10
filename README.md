# Práctica D2 — Del enunciado al programa

## Autores

Alejandro García Da Silva  
Carlos Manzano Esclapez

## Análisis

Una tienda aplica descuentos dependiendo del importe de la compra.

### Entradas

- Importe total de la compra.

### Salidas

- Importe de la compra.
- Porcentaje de descuento aplicado.
- Cantidad descontada.
- Precio final después del descuento.

### Restricciones

- Si la compra es menor de 100 €, no se aplica descuento.
- A partir de 100 €, se aplica un descuento del 10 %.
- A partir de 300 €, se aplica un descuento del 15 %.
- El importe de la compra debe ser un número.

## Diseño

### Pseudocódigo

Algoritmo DescuentoTienda
    Leer importe

    Si importe >= 300 Entonces
        porcentaje_descuento ← 0.15
    Si no
        Si importe >= 100 Entonces
            porcentaje_descuento ← 0.10
        Si no
            porcentaje_descuento ← 0
        Fin Si
    Fin Si

    descuento ← importe * porcentaje_descuento
    precio_final ← importe - descuento

    Escribir porcentaje_descuento
    Escribir descuento
    Escribir precio_final
Fin Algoritmo

# Diagrama de flujo hecho en el PDF
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
- Si el importe es menor de 100 €, no hay descuento.
- Desde 100 € (incluido) hasta menos de 300 € se aplica un 10 %.
- Desde 300 € (incluido) se aplica un 15 %.
- Los descuentos no se acumulan: se aplica solo el mayor que corresponda.
- El importe se introduce con punto decimal (por ejemplo, 99.99) y se supone mayor o igual que 0.
- Los importes se muestran con dos decimales.

## Diseño

### Pseudocódigo

INICIO
    UMBRAL_BAJO ← 100
    UMBRAL_ALTO ← 300
    DESCUENTO_BAJO ← 0.10
    DESCUENTO_ALTO ← 0.15

    LEER importe

    SI importe >= UMBRAL_ALTO ENTONCES
        porcentaje ← DESCUENTO_ALTO
    SI NO, SI importe >= UMBRAL_BAJO ENTONCES
        porcentaje ← DESCUENTO_BAJO
    SI NO
        porcentaje ← 0
    FIN SI

    descuento ← importe * porcentaje
    total ← importe - descuento

    ESCRIBIR importe, descuento, porcentaje, total
FIN

# Diagrama de flujo hecho en el PDF
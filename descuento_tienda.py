"""Calcula el descuento y el total a pagar de una compra.

La tienda aplica un 10 % de descuento a partir de 100 € de compra
y un 15 % a partir de 300 €. Los descuentos no se acumulan.

Módulo: Programación
UD 2: Primeros pasos con Python · Práctica D2
Autor: Alejandro García Da Silva y Carlos Manzano Esclapez
"""

# Constantes
UMBRAL_DESCUENTO_BAJO = 100.0
UMBRAL_DESCUENTO_ALTO = 300.0
DESCUENTO_BAJO = 0.10
DESCUENTO_ALTO = 0.15


def calcular_porcentaje(importe):
    """Devuelve el porcentaje de descuento que corresponde a un importe."""
    if importe >= UMBRAL_DESCUENTO_ALTO:
        return DESCUENTO_ALTO
    elif importe >= UMBRAL_DESCUENTO_BAJO:
        return DESCUENTO_BAJO
    else:
        return 0.0


def main():
    # 1. Entrada
    importe = float(input("Importe de la compra (€): "))

    # 2. Proceso
    porcentaje = calcular_porcentaje(importe)
    descuento = importe * porcentaje
    total = importe - descuento

    # 3. Salida
    print(f"\nImporte:   {importe:8.2f} €")
    print(f"Descuento: {descuento:8.2f} € ({porcentaje * 100:.0f} %)")
    print(f"Total:     {total:8.2f} €\n")


if __name__ == "__main__":
    main()
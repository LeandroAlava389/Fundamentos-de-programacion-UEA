def calcular_descuento(monto_total, descuento=10):
    """
    parámetro monto_total: Monto total de la compra.
    parámetro descuento: Porcentaje de descuento
    """
    descuento = (monto_total * descuento) / 100
    return descuento

# Solicitar datos al usuario
monto1 = float(input("Ingrese el monto total de la compra: "))
descuento_predeterminado = calcular_descuento(monto1)
monto_final1 = monto1 - descuento_predeterminado
print(f"Compra de ${monto1}: Descuento de ${descuento_predeterminado}, Monto final a pagar: ${monto_final1}")

# Solicitar datos al usuario con un porcentaje de descuento personalizado
monto2 = float(input("Ingrese el monto total de la segunda compra: "))
descuento_personalizado = float(input("Ingrese el porcentaje de descuento: "))

descuento2 = calcular_descuento(monto2, descuento_personalizado)
monto_final2 = monto2 - descuento2
print(f"Compra de ${monto2}: Descuento de ${descuento2} ({descuento_personalizado}%), Monto final a pagar: ${monto_final2}")
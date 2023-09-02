

#------------------ Michael Morron ----------------

def calcular_costo_estacionamiento(dia_semana, hora_inicio, dia_fin, hora_fin):
    tarifas = {"lunes": 2.00, "martes": 2.00, "miercoles": 2.00, "jueves": 2.50, "viernes": 2.50, "sabado": 3.00, "domingo": 3.00}
    
    if dia_semana not in tarifas:
        return None
    
    tarifa = tarifas[dia_semana]
    # damos valores a las horas de inicio y fin
    inicio = hora_inicio[0] * 60 + hora_inicio[1]
    fin = hora_fin[0] * 60 + hora_fin[1]
    
    tiempo_total = fin - inicio
    
    if tiempo_total < 0:
        tiempo_total += 24 * 60
    
    if tiempo_total <= 5:
        tiempo_total = 0
    elif tiempo_total % 60 > 5:
        tiempo_total += 60
    # por medio de los if calculamos el costo de la tarifa
    costo_total = tarifa * tiempo_total / 60
    return costo_total

try:
    dia_inicio = input("Ingrese el día de inicio (de Lunes a Domingo): ").lower()
    hora_inicio = [int(x) for x in input("Ingrese la hora de inicio (HH:MM) En Formato de 24 Horas: ").split(":")]
    dia_fin = input("Ingrese el día de finalización (de Lunes a Domingo): ").lower()
    hora_fin = [int(x) for x in input("Ingrese la hora de finalización (HH:MM) En Formato de 24 Horas: ").split(":")] # añado un split para que divida hora de minutos con " : "
    
    costo = calcular_costo_estacionamiento(dia_inicio, hora_inicio, dia_fin, hora_fin)
    
    # imprimo el valor del costo total
    if costo is not None:
        print("El costo de estacionamiento es: ",costo)
    else:
        print("Día de la semana inválido. Por favor, ingrese un día válido.")
except ValueError:
    print("Error: Ingrese valores numéricos válidos para las horas y minutos.")

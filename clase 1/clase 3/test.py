
def verificar_calificacion(notas):
    nota_para_aprobar = 6
    sumatoria_notas = 0
    cantidad_notas = 0  
    for nota in notas:
        sumatoria_notas += nota
        cantidad_notas += 1

    promedio_notas = (sumatoria_notas / cantidad_notas)
    if promedio_notas >= nota_para_aprobar:
        return 'Aprobado'
    else:
        return 'Reprobado'

#Pruebas
notas_prueba = [6, 6, 6]
resultado = verificar_calificacion(notas_prueba)
print ('El estado del examen es:', resultado)
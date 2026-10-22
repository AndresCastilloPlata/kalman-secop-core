
def procesar_contratos_secop( datos_crudos, nombre_departamento):
    total_contratos = len(datos_crudos)
    
    contratos_por_departamento = 0
    
    for contrato in datos_crudos:

        if contrato['departamento'] == nombre_departamento :
            contratos_por_departamento += 1
    
    return total_contratos, contratos_por_departamento
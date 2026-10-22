
def procesar_contratos_secop( datos_crudos):
    total_contratos = len(datos_crudos)
    
    contratos_atlantico = 0
    
    for contrato in datos_crudos:

        if contrato['departamento'] == 'Atlántico' :
            contratos_atlantico += 1
    
    return total_contratos, contratos_atlantico
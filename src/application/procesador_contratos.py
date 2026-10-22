
def procesar_contratos_secop( datos_crudos, nombre_departamento):
    
    mapa_tildes = str.maketrans('áéíóú', 'aeiou')
    departamento_limpio = nombre_departamento.lower().translate(mapa_tildes)
    
    total_contratos = len(datos_crudos)
    contratos_por_departamento = 0
    
    for contrato in datos_crudos:

        if contrato['departamento'].lower().translate(mapa_tildes) == departamento_limpio :
            contratos_por_departamento += 1
    
    return total_contratos, contratos_por_departamento
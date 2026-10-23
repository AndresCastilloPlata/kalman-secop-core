from src.application.procesador_contratos import procesar_contratos_secop


def test_procesar_contratos_secop_un_solo_departamento():
    # Arrange
    datos_prueba = [
        {'departamento': 'Atlántico'}
    ]

    departamento_prueba = 'atlantico'

    # Act
    total_prueba, contratos_prueba = procesar_contratos_secop(datos_prueba, departamento_prueba)
    
    # Assert
    assert total_prueba == 1
    assert contratos_prueba == 1
    
def test_procesar_contratos_secop_un_solo_departamento_falso():
    # Arrange
    datos_prueba = [
        {'departamento': 'Bogotá'}
    ]

    departamento_prueba = 'atlantico'

    # Act
    total_prueba, contratos_prueba = procesar_contratos_secop(datos_prueba, departamento_prueba)
    
    # Assert
    assert total_prueba == 1
    assert contratos_prueba == 0
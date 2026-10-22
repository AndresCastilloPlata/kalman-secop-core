from fastapi import FastAPI
from src.infrastructure.config import MAX_ROWS_LIMIT
from src.infrastructure.socrata_client import fetch_secop_data  
from src.application.procesador_contratos import procesar_contratos_secop

app = FastAPI(title='Kalman SECOP Core')

@app.get('/')
def read_root():
    return {'estado': 'Sistema energizado y en linea ⚡️',
            'limite_datos_permitidos': MAX_ROWS_LIMIT
            }
    
@app.get('/api/v1/contratos/{departamento}')
async def obtener_contratos(departamento):
    datos_crudos = await fetch_secop_data()
    total, contratos = procesar_contratos_secop(datos_crudos, departamento)
    return { 'total_nacional': total, 'total_departamento': contratos}
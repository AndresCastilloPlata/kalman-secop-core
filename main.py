from fastapi import FastAPI
from src.infrastructure.config import MAX_ROWS_LIMIT
from src.infrastructure.socrata_client import fetch_secop_data  

app = FastAPI(title='Kalman SECOP Core')

@app.get('/')
def read_root():
    return {'estado': 'Sistema energizado y en linea ⚡️',
            'limite_datos_permitidos': MAX_ROWS_LIMIT
            }
    
@app.get('/api/v1/contratos')
async def obtener_contratos():
    return await fetch_secop_data()
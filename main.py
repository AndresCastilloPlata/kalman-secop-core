from fastapi import FastAPI
from src.infrastructure.config import MAX_ROWS_LIMIT

app = FastAPI(title='Kalman SECOP Core')

@app.get('/')
def read_root():
    return {'estado': 'Sistema energizado y en linea ⚡️',
            'limite_datos_permitidos': MAX_ROWS_LIMIT
            }
import httpx
from src.infrastructure.config import SOCRATA_APP_TOKEN, SECOP_DATASET_ID, MAX_ROWS_LIMIT


async def fetch_secop_data():
    async with httpx.AsyncClient(timeout=30.0) as client:
        url = f"https://www.datos.gov.co/resource/{SECOP_DATASET_ID}.json"
        
        respuesta = await client.get(
            url,
            params={
                '$limit': MAX_ROWS_LIMIT,
                '$$app_token': SOCRATA_APP_TOKEN
            }
        )
        
        # fusible por falla el servidor del Estado
        respuesta.raise_for_status()
        
        # Demodulador: estrae la carga util
        datos_crudos = respuesta.json()
        
        return datos_crudos
    
    

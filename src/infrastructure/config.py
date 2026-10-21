import os
from dotenv import load_dotenv

load_dotenv()

SOCRATA_APP_TOKEN = os.getenv('SOCRATA_APP_TOKEN')
SECOP_DATASET_ID = os.getenv('SECOP_DATASET_ID')

MAX_ROWS_LIMIT = int(os.getenv('MAX_ROWS_LIMIT'))
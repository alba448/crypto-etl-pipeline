import logging
import os
from datetime import datetime
from src.extract import fetch_crypto_data
from src.transform import transform_data
from src.load import upload_to_s3
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    load_dotenv()
    BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "tu-bucket-de-prueba")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        logging.info("--- INICIANDO PIPELINE ETL ---")
        
        # 1. Extract
        raw_data = fetch_crypto_data()
        
        # 2. Transform
        clean_df = transform_data(raw_data)
        
        # 3. Load
        file_name = f"crypto_data_{timestamp}"
        upload_to_s3(clean_df, BUCKET_NAME, file_name)
        
        logging.info("--- PIPELINE FINALIZADO CON ÉXITO ---")
        
    except Exception as e:
        logging.critical(f"El pipeline falló: {e}")

if __name__ == "__main__":
    run_pipeline()
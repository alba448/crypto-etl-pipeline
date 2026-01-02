import boto3
import logging
import os
from io import BytesIO

def upload_to_s3(df, bucket_name, file_name):
    logging.info(f"Iniciando carga en S3: {file_name}.parquet")
    
    is_local = os.getenv("ENV") == "local"
    endpoint = "http://localhost:4566" if is_local else None
    
    try:
        parquet_buffer = BytesIO()
        df.to_parquet(parquet_buffer, index=False, engine='pyarrow')
        
        s3 = boto3.client('s3', endpoint_url=endpoint)
        
        if is_local:
            try:
                s3.create_bucket(Bucket=bucket_name)
            except s3.exceptions.BucketAlreadyExists:
                pass

        s3.put_object(
            Bucket=bucket_name,
            Key=f"gold/crypto/{file_name}.parquet",
            Body=parquet_buffer.getvalue()
        )
        logging.info(f"Carga completada exitosamente en {'LocalStack' if is_local else 'AWS'}.")
        
    except Exception as e:
        logging.error(f"Error al cargar en S3: {e}")
        raise
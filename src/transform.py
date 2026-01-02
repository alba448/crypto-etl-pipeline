import pandas as pd
import logging

def transform_data(raw_data):
    logging.info("Iniciando transformación de datos con Pandas...")
    df = pd.DataFrame(raw_data)
    
    cols = ['id', 'symbol', 'current_price', 'market_cap', 'total_volume', 'last_updated']
    df = df[cols]
    
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    
    mean_volume = df['total_volume'].mean()
    df['volume_category'] = df['total_volume'].apply(
        lambda x: 'High' if x > mean_volume else 'Low'
    )
    
    return df
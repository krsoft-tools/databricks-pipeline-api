import pandas as pd
from app.schemas import MetricsOutput

def process_pipeline_data(file_path: str, category: str = None, min_value: float = 0.0):
    df = pd.read_csv(file_path)
    
    if category:
        df = df[df['category'] == category]
    
    df = df[df['value'] >= min_value]
    
    metrics = MetricsOutput(
        total_records=len(df),
        avg_value=float(df['value'].mean()) if not df.empty else 0.0,
        max_value=float(df['value'].max()) if not df.empty else 0.0
    )
    
    return len(df), metrics
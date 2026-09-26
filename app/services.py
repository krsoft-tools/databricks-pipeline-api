import pandas as pd
from app.schemas import MetricsOutput

def process_pipeline_data(file_path: str, category: str = None, min_value: float = 0.0):
    df = pd.read_csv(file_path)
    
    # 1. Bezpečné filtrovanie podľa kategórie (hľadá stĺpec bez ohľadu na veľké/malé písmená)
    if category:
        cat_col = next((col for col in df.columns if col.lower() == 'category'), None)
        if cat_col:
            df = df[df[cat_col].astype(str).str.lower() == category.lower()]
    
    # 2. Bezpečné filtrovanie podľa hodnoty (hľadá stĺpec value, amount, sales, total atď.)
    val_col = next((col for col in df.columns if col.lower() in ['value', 'amount', 'sales', 'total', 'price']), None)
    
    # Ak nenašiel presný názov, vezme prvý číselný stĺpec v CSV
    if not val_col:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            val_col = numeric_cols[0]

    if val_col and min_value > 0.0:
        df = df[df[val_col] >= min_value]
    
    # 3. Výpočet metrík cez tvoj Pydantic model
    if val_col and not df.empty:
        avg_val = float(df[val_col].mean())
        max_val = float(df[val_col].max())
    else:
        avg_val = 0.0
        max_val = 0.0

    metrics = MetricsOutput(
        total_records=len(df),
        avg_value=round(avg_val, 2),
        max_value=round(max_val, 2)
    )
    
    return len(df), metrics
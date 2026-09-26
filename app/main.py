from fastapi import FastAPI, HTTPException
from app.schemas import DataSummaryRequest, PipelineResponse
from app.services import process_pipeline_data

app = FastAPI(
    title="Databricks Data Pipeline API",
    description="Production-ready FastAPI layer serving cleaned Databricks pipeline outputs.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "online", "service": "Databricks Pipeline API"}

@app.post("/api/v1/process-summary", response_model=PipelineResponse)
def get_summary(payload: DataSummaryRequest):
    try:
        # Cesta k vzorkovým dátam
        count, metrics = process_pipeline_data(
            file_path="data/sales_summary.csv",
            category=payload.category,
            min_value=payload.min_value
        )
        return PipelineResponse(
            status="success",
            processed_count=count,
            metrics=metrics
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
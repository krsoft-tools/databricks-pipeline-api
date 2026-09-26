from pydantic import BaseModel
from typing import List, Optional

class DataSummaryRequest(BaseModel):
    category: Optional[str] = None
    min_value: Optional[float] = 0.0

class MetricsOutput(BaseModel):
    total_records: int
    avg_value: float
    max_value: float

class PipelineResponse(BaseModel):
    status: str
    processed_count: int
    metrics: MetricsOutput
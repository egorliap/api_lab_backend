from datetime import datetime

from pydantic import BaseModel, Field


class SConversionRates(BaseModel):
    updated_at: datetime = Field(..., validation_alias="time_last_update_unix", description="Last update time")
    conversion_rates: dict = Field(..., description="Conversion rates of currency")
    
class SPairConversion(BaseModel):
    base_code: str = Field(..., description="Currency code, from which to convert")
    target_code: str = Field(..., description="Currency code, to which to convert")
    conversion_rate: float = Field(..., description="Conversion rate, from base to target currency")
    conversion_result: float|None = Field(..., description="Converted amount (default = 1)")
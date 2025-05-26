from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class BaseSchema(BaseModel):
    """
    Base schema for all models in the application.
    """
    class Config:
        # Allow arbitrary types for fields
        arbitrary_types_allowed = True
        # Allow extra fields in the model
        extra = "allow"
        # Use snake_case for field names in JSON serialization
        alias_generator = lambda x: x.lower()
        # Use JSON-compatible data types for serialization
        json_encoders = {
            Any: lambda v: str(v),
            List: lambda v: [str(i) for i in v],
            Dict: lambda v: {str(k): str(v) for k, v in v.items()}
        }

    webhook: Optional[str] = Field(
        None,
        description="Webhook URL for receiving notifications."
    )
    track_id : Optional[str] = Field(
        None,
        description="Track ID for tracking purposes."
    )
    
class FetchSchema(BaseModel):
    """
    Schema for fetching data from the API.
    """
    id: str = Field(
        ...,
        description="ID of the item to fetch."
    )
    key: str = Field(
        ...,
        description="API key for authentication."
    )
    

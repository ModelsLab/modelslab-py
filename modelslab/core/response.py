from pydantic import BaseModel, Field

from typing import Any, Optional, List, Dict, Union


class ResponseSchema(BaseModel):
    data: Optional[Union[str, List[Dict[str, Any]]]] = Field(
        None,
        description="Data associated with the response."
    )
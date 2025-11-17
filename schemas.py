from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Unity/Gamedev portfolio schemas

class Contact(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Reply-to email")
    message: str = Field(..., min_length=5, max_length=5000, description="Message body")

class Project(BaseModel):
    title: str = Field(..., description="Project title")
    description: Optional[str] = Field(None, description="Summary")
    tags: List[str] = Field(default_factory=list, description="Labels for filtering")
    media_url: Optional[str] = Field(None, description="Cover image or video URL")
    featured: bool = Field(False, description="Show on homepage")

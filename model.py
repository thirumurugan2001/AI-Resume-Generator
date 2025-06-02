from pydantic import BaseModel

class ResumeRequest(BaseModel):
    name: str 
    email: str
    phone: str
    skills: str
    experience: str 
    summary: str
    linked_in: str
    degree: str
    university: str
    grad_year:  str
    projects: str
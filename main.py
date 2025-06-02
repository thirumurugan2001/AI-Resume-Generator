from fastapi import FastAPI
import uvicorn
from model import ResumeRequest
from ConnectAi import generate_resume_with_gpt
app = FastAPI()


@app.post("/resume/generation")
async def createResume(resume_data: ResumeRequest):
    try :
        response  = generate_resume_with_gpt(
            resume_data.name,
            resume_data.email,
            resume_data.phone,
            resume_data.skills,
            resume_data.experience,
            resume_data.summary,
            resume_data.linked_in,
            resume_data.degree,
            resume_data.university,
            resume_data.grad_year,
            resume_data.projects
        )
        return response
    except Exception as e:
        print("Error in the createResume",str(e))
        return {
            "message": str(e),
            "stratusCode": 400,
            "status":False
        }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
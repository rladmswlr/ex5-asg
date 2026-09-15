from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/items")
def get_items():
    return [
        {
            "email": "student01@example.com",
            "name": "테스트 사용자",
            "class_name": "MSP 6기",
            "kor": 90,
            "eng": 85,
            "mat": 95
        }
    ]


@app.get("/health")
def health():
    return {"status": "ok"}

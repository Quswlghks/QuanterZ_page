from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 정적 파일 경로 설정
app.mount("/css", StaticFiles(directory="page/css"), name="css")
app.mount("/js", StaticFiles(directory="page/js"), name="js")
app.mount("/assets", StaticFiles(directory="page/assets"), name="assets")

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="page")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # 'index.html'을 렌더링하여 반환합니다.
    return templates.TemplateResponse("index.html", {"request": request})

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="IcanDoIt - 아이폰 쉬운 가이드")

app.mount('/static', StaticFiles(directory='app/static'), name='static')
templates = Jinja2Templates(directory='app/templates')


@app.get('/', response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={
            'menu_items': [
                {
                    'id': 'sms',
                    'title': '문자 메시지 보내기',
                    'description': '아이폰에서 가장 쉬운 첫걸음',
                }
            ]
        },
    )

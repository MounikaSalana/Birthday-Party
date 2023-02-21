from fastapi import FastAPI,Request, Form, status
from fastapi.templating import Jinja2Templates
from models.user import userdatamodel
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="html_templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

userBirthDays = []


@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "birthdays": userBirthDays})
    
@app.post('/save_form_data')
def save_form_data(name: str = Form(...), year: str = Form(...), month: str = Form(...), date: str = Form(...)):
    

    data = userdatamodel(name=name, year=year, month=month, date=date)
    userBirthDays.append(data)
    print(data)
    print(userBirthDays)
    return RedirectResponse(url=app.url_path_for("root"), status_code=status.HTTP_303_SEE_OTHER)
    
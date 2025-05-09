from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.routers import auth, ipca, users

app = FastAPI()

app.include_router(ipca.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
async def redirect_to_docs():
    return RedirectResponse(url="/docs", status_code=302)
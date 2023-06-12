from fastapi import FastAPI

from app.controllers.register_process_controller import router


app = FastAPI()

app.include_router(router)

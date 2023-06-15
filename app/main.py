from fastapi import FastAPI

from app.controllers.process_controller import router as process
from app.controllers.document_controller import router as document

app = FastAPI()

app.include_router(process)
app.include_router(document)

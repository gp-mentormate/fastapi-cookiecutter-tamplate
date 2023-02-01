import logging
from fastapi import APIRouter 

from sample_app.schemas import SampleSchema

logger = logging.getLogger(__name__)
router = APIRouter(prefix='/sample_app', tags=["Sample App"])


@router.get("/sample_route", response_model=SampleSchema)
async def sample_route():
    resp = SampleSchema(name='Hello world')
    return resp

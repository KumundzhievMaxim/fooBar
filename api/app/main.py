from fastapi import FastAPI, HTTPException

from app.models.response import Response
from app.utilities.google_trends_helper import pull_search_interest


app = FastAPI()


@app.get("/search_interest/{keyword}", response_model=Response)
async def search_interest_by_keyword(keyword: str):
    """ Endpoint which return ordered collection of search scores for required keyword. """

    try:
        response = pull_search_interest(keyword=keyword)
    except HTTPException as e:
        raise e

    return Response(search_interest=response)

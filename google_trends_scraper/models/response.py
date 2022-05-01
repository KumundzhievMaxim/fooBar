from pydantic import BaseModel


class KeyWordSchema(BaseModel):
    key_word: str
    key_word_suggestion: int
    key_word_interest_score: int
    key_word_interest_over_time: int
    request_timestamp: str
    request_status: int
    request_error: str


class GoogleTrendsAPIResponse(BaseModel):
    entity: KeyWordSchema




# respone = {'entity': {
#                 'name': 'test',
#                 'interest_score': 10,
#                 'interest_over_time': 10,
#                 'request_timestamp': '10:22:09:01',
#                 'request_status': 200,
#                 'request_error': ''
#                 }
#         }
#
# print(GoogleTrendsAPIResponse.parse_obj(respone).dict())
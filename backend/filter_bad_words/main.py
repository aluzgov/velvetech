from enum import Enum
from typing import Optional

from pydantic.main import BaseModel
from starlette import status
from starlette.responses import Response

from filter_bad_words.app import create_app
from filter_bad_words.services import EnUsFilterBadWords

app = create_app()


class FilterResponse(BaseModel):
    filtered_phrase: str
    error_message: Optional[str]


class Locale(str, Enum):
    en_US = "en_US"


bad_words_filters = {
    'en_US': EnUsFilterBadWords()
}


@app.get('/api/filter-bad-words/{locale}/', response_model=FilterResponse)
async def filter_bad_words(locale: Locale, raw_phrase: str, response: Response):
    bad_words_filter = bad_words_filters.get(locale)
    if bad_words_filter is None:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {
            "filtered_phrase": "",
            "error_message": f"Filter for {locale} not found."
        }

    return {
        "filtered_phrase": bad_words_filter.filter_bad_words(raw_phrase),
    }

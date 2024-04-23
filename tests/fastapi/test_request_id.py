import logging

import pytest

from matter_observability.fastapi.request_id import (
    RequestIdLogFilter,
    _request_id_ctx_var,
    get_request_id,
    process_request_id,
)


@pytest.mark.asyncio
async def test_can_extract_request_id_from_request_and_retrieve_it_from_context(mocker):
    request = mocker.Mock()
    request.headers = {"x-request-id": "1234"}
    await process_request_id(request, mocker.AsyncMock())

    assert get_request_id() == "1234"


@pytest.mark.asyncio
async def test_logger_filter_can_get_request_id_from_context(mocker):
    _request_id_ctx_var.set("1234")

    my_filter = RequestIdLogFilter()
    my_record = mocker.Mock()
    my_filter.filter(my_record)

    assert my_record.request_id == "1234"

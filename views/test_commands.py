import pytest


from views.commands import (
    validate_date,
)


@pytest.fixture



@pytest.mark.parametrize("date, result", [("2020-11-03", True), ("2019-12-31", True), ("0001-01-01", True),
                                          ("2020-13-03", False), ("2020-11-32", False), ("2020-1103", False),
                                          ("2020-00-00", False), ("2020", False), ("ewff", False),("", False)])
def test_validate_date_parametrize(date, result):
    assert validate_date(date) == result

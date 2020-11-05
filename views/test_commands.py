import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from views.commands import (
    validate_date, is_exist_task
)


@pytest.fixture
def connect_db():
    engine = create_engine('sqlite:///db.sqlite3')
    session = sessionmaker(bind=engine)()
    return session


@pytest.mark.parametrize("date, event, result",
                         [("0001-01-01", "1", False), ("0001-01-02", "2", False)])
def test_is_exist_task(connect_db, date, event, result):
    assert is_exist_task(connect_db, date, event) == result


@pytest.mark.parametrize("date, result", [("2020-11-03", True), ("2019-12-31", True), ("0001-01-01", True),
                                          ("2020-13-03", False), ("2020-11-32", False), ("2020-1103", False),
                                          ("2020-00-00", False), ("2020", False), ("ewff", False),("", False)])
def test_validate_date_parametrize(date, result):
    assert validate_date(date) == result

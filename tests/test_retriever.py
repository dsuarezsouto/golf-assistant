import pytest
from src.utils import load_document
@pytest.mark.unit
def test_load_document():
    docs = load_document('src/golf_manuals/FS_Golfers_Guide_1.pdf')
    print(docs)
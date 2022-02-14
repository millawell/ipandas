import pdb
from mwl_ipandas import __version__
from mwl_ipandas.main import load_dataframe, input_valid
from pathlib import Path

tmp_path = Path('tmp')

CSV_FILE_CONTENT = """
id,name,age
1,John,20
2,Jane,21
"""


def test_version():
    assert __version__ == '0.1.0'


def test_load_csv():
    d = tmp_path / "hello.csv"
    d.write_text(CSV_FILE_CONTENT)
    df = load_dataframe(d)
    assert tuple(df.columns) == ('id', 'name', 'age')
    

def test_load_pickle():
    d = tmp_path / "hello.csv"
    d.write_text(CSV_FILE_CONTENT)
    df = load_dataframe(d)
    df.to_pickle(tmp_path / "hello.pkl")
    df2 = load_dataframe(tmp_path / "hello.pkl")
    assert tuple(df2.columns) == ('id', 'name', 'age')

def test_input_valid():
    d = tmp_path / "hello.csv"
    d.write_text("_")
    assert input_valid(d)
    d = tmp_path / "hello.pkl"
    d.write_text("_")
    assert input_valid(d)
    d = tmp_path / "hello.pickle"
    assert not input_valid(d)



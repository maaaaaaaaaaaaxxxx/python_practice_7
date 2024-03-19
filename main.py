import pytest, os
import pandas as pd
from app.io.input import coninput, readfile, pd_readfile
from app.io.output import conoutput, writefile, pd_writefile
import io

def main():
    # print("a")
    # coninput()
    # a = readfile('text.txt')
    # b = pd_readfile('text.txt')
    # conoutput('test')
    # writefile('text.txt', 'abcdefg')
    # pd_writefile('test.csv', '{}')
    file_path = "text.txt"
    csv_file_path = "test.csv"

    # Test cases for readfile function
    def test_readfile_returns_file_object():
        file_object = readfile(file_path)
        assert isinstance(file_object, io.TextIOWrapper)

    def test_readfile_handles_nonexistent_file():
        with pytest.raises(FileNotFoundError):
            readfile("nonexistent_file.txt")

    def test_readfile_read_content_correctly():
        with open(file_path, "r") as file:
            expected_content = file.read()
        file_object = readfile(file_path)
        assert file_object.read() == expected_content

    # Test cases for pd_readfile function
    def test_pd_readfile_returns_dataframe():
        df = pd_readfile(csv_file_path)
        assert isinstance(df, pd.DataFrame)

    def test_pd_readfile_handles_nonexistent_file():
        with pytest.raises(FileNotFoundError):
            pd_readfile("nonexistent_file.csv")

    def test_pd_readfile_read_content_correctly():
        expected_df = pd.read_csv(csv_file_path)
        df = pd_readfile(csv_file_path)
        pd.testing.assert_frame_equal(df, expected_df)
    test_readfile_returns_file_object()
    test_readfile_handles_nonexistent_file()
    test_readfile_read_content_correctly()
    test_pd_readfile_returns_dataframe()
    test_pd_readfile_handles_nonexistent_file()

main()
import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root_path)

sys.path.append(project_root_path)
import src.my_library.predict_polarity as predict_polarity

def test_predict_positive():
    input_statistics = [5, 1]
    expected_output = 'positive'
    assert predict_polarity.predict(input_statistics) == expected_output

def test_predict_negative():
    input_statistics = [1, 4]
    expected_output = 'negative'
    assert predict_polarity.predict(input_statistics) == expected_output

def test_predict_neutral():
    input_statistics = [3, 3]
    expected_output = 'neutral'
    assert predict_polarity.predict(input_statistics) == expected_output

def test_predict_empty():
    input_statistics = []
    expected_output = 'neutral'
    assert predict_polarity.predict(input_statistics) == expected_output


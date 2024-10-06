import numpy as np

from python_ml_project_api.prediction import predict


def test_prediction_simple():
    in_data = np.array([1, 2, 3, 1])
    expected_data = 7

    result = predict(in_data)

    assert expected_data == result

import pytest





from practice.python_morsels import get_earliest





@pytest.mark.parametrize(
        'input_vals,output' , [
            ("01/27/1832", "01/27/1756"), "01/27/1756"),
            ("02/29/1972", "12/21/1946"), "12/21/1946"),
            ("02/24/1946", "03/21/1946"),"02/24/1946"),
            ("02/24/1946", "01/29/1946", "03/29/1945"), "03/29/1945"),
            ]
        )
def test_earliest(input_vals, output):
    """
    test the earliest function
    """
    assert get_earliest(input_vals)==output


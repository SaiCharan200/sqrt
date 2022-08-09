import math
import pytest
@pytest.mark.parametrize("num, output",[(4,2),(9,3),(144,12)])
def square_rt(num,output):
 assert math.sqrt(num) == output


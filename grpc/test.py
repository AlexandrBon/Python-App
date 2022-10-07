import pytest
import grpc
from definitions.builds.service_pb2 import Null, Numbers
from definitions.builds.service_pb2_grpc import TestServiceStub


def test():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        @pytest.mark.parametrize("test_input, expected",
                                 [
                                     (client.calcSum(Numbers(a=1, b=6)), 7),
                                     (client.calcSum(Numbers(a=1, b=-1)), 0)
                                 ]
                                 )
        def test_eval(test_input, expected):
            assert test_input == expected

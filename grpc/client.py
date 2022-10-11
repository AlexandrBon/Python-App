# client.py
# -*- coding: utf-8 -*-

import grpc
from definitions.builds.service_pb2 import Null, Numbers
from definitions.builds.service_pb2_grpc import TestServiceStub


def execute_client():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        summa = client.calcSum(Numbers(
            a=5,
            b=100
        ))

        print(summa.sum)


if __name__ == "__main__":
    execute_client()
    
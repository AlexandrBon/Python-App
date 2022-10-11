# server.py
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

import grpc
from definitions.builds.service_pb2 import Summa
from definitions.builds.service_pb2_grpc import (
    TestServiceServicer, add_TestServiceServicer_to_server)


class Service(TestServiceServicer):
    def Health(self, request, context):
        return request

    def calcSum(self, request, context):
        return Summa(sum=request.a + request.b)


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
    
import worker
import new_task
import sys
import os
import db


def test():
    new_task.send_data({"@user": [[1, 2], [0, 1]]})
    print(db.results)



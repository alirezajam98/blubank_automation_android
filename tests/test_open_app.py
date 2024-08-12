import time
import pytest


def test_open_app(create_driver_fixture):
    driver = create_driver_fixture

    # برنامه را برای 30 ثانیه باز نگه دارید
    time.sleep(15)

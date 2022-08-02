######################################################################
#
# File: test/integration/conftest.py
#
# Copyright 2020 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

import sys

import pytest


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        '--sut',
        default=f'{sys.executable} -m b2',
        help='Path to the System Under Test',
    )

    parser.addoption('--cleanup', action='store_true', help='Perform full cleanup at exit')


@pytest.fixture(scope='session')
def sut(request):
    return request.config.getoption('--sut')


@pytest.fixture(scope='session')
def cleanup(request):
    return request.config.getoption('--cleanup')

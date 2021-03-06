"""
Simple hostname test (on host).

Before this test please set your hostname to something meaningful.

:difficulty: simple
:copyright: 2014 Red Hat Inc.
"""
import logging

from avocado.utils import process
from virttest.compat_52lts import results_stdout_52lts


def run(test, params, env):
    """
    Logs the host name and exits

    :param test: QEMU test object
    :param params: Dictionary with the test parameters
    :param env: Dictionary with test environment.
    """
    result = process.run("hostname")
    logging.info("Output of 'hostname' cmd is '%s'",
                 results_stdout_52lts(result))

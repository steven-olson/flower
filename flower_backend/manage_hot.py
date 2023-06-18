#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def debug():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_core.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line([
        "manage.py",
        "runserver",
        "--no_reload"
    ])


def pytest():
    import pytest

    #pytest.main(args=["flower_testing.tests.test_smoke.test_basic.py::test_task_simple","--reuse-db", "-v"])
    pytest.main(args=["--reuse-db", "-v"])


if __name__ == '__main__':
    pytest()


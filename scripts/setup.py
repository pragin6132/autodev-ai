#!/usr/bin/env python3
"""
AutoDev AI Package Configuration Script.

Allows the project to be installed in editable mode for local development.
"""

from setuptools import find_packages, setup

setup(
    name="autodev-ai",
    version="0.1.0",
    description="Autonomous Multi-Agent Software Engineering Platform powered by MCP",
    author="AutoDev AI Authors",
    packages=find_packages(where="backend"),
    package_dir={"": "backend"},
    python_requires=">=3.11",
    install_requires=[
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "python-dotenv>=1.0.0",
        "SQLAlchemy>=2.0.0",
        "alembic>=1.12.0",
        "websockets>=12.0",
        "structlog>=23.2.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
)

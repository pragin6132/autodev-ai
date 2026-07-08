#!/usr/bin/env python3
"""
AutoDev AI Project Initialization Script.

Verifies system requirements, configures local environment variables,
and verifies required directory folders.
"""

import os
import shutil
import sys

REQUIRED_DIRECTORIES = [
    "agents/team_lead",
    "agents/planner",
    "agents/frontend_agent",
    "agents/backend_agent",
    "agents/tester",
    "agents/devops",
    "backend/app",
    "config",
    "database",
    "docker",
    "docs",
    "frontend/src",
    "frontend/public",
    "mcp/client",
    "mcp/servers",
    "mcp/tools",
    "scripts",
    "tests/backend",
    "tests/frontend",
]


def check_python_version() -> None:
    """Ensure python execution environment meets standards."""
    major, minor = sys.version_info.major, sys.version_info.minor
    if major < 3 or (major == 3 and minor < 11):
        print(f"[ERROR] AutoDev AI requires Python 3.11+. Current: {major}.{minor}")
        sys.exit(1)
    print("[OK] Python version verification succeeded.")


def initialize_directories() -> None:
    """Verify and initialize workspace directories."""
    print("Verifying directory structure...")
    for dir_path in REQUIRED_DIRECTORIES:
        os.makedirs(dir_path, exist_ok=True)
    print("[OK] Workspace directories verified.")


def initialize_env_file() -> None:
    """Setup active environment settings template."""
    env_file = ".env"
    example_env = ".env.example"

    if os.path.exists(env_file):
        print("[INFO] Active '.env' file already exists. Skipping initialization.")
        return

    if not os.path.exists(example_env):
        print(f"[ERROR] Configuration template '{example_env}' not found.")
        sys.exit(1)

    try:
        shutil.copy(example_env, env_file)
        print("[OK] Initialized new '.env' from environment template.")
    except IOError as e:
        print(f"[ERROR] Failed to write '.env': {e}")
        sys.exit(1)


def main() -> None:
    print("==================================================")
    print("AutoDev AI Project Initializer")
    print("==================================================")
    check_python_version()
    initialize_directories()
    initialize_env_file()
    print("==================================================")
    print("[SUCCESS] Project initialization completed successfully!")
    print("==================================================")


if __name__ == "__main__":
    main()

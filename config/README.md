# Configuration Layer

This directory stores configuration loaders, rules, settings files, and service setups.

---

## Files

- **`settings.py`**: A Pydantic BaseSettings class loading configuration keys from active environmental scopes and falling back to SQLite parameters.

## Configuration Profiles

Configurations are controlled by setting the `APP_ENV` environment variable:

- **`development`**: Configures verbose console log formats, enables hot-reload flags, and directs database writes to the local SQLite database container.
- **`production`**: Limits logs to level INFO, enforces HTTPS requirements, and establishes connections directly with the remote PostgreSQL database.

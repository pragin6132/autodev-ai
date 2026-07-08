# Database Schema & Migrations

This directory manages the storage schema configuration, tables initialization, and migrations for AutoDev AI.

---

## Setup & Running Migrations

Database operations are managed via **SQLAlchemy ORM** and version-controlled via **Alembic** migrations in the backend application.

### Local Development (SQLite)
By default, the backend configures a local SQLite file database `sqlite:///./autodev.db` if no environment variables are defined.

### Production Setup (PostgreSQL)
Ensure you set the `DATABASE_URL` parameter in `.env`:
```bash
DATABASE_URL=postgresql://autodev:autodev_password@localhost:5432/autodev_db
```

### Initializing the Schema
To initialize the database tables manually using the schema file:
```bash
psql -U autodev -d autodev_db -f schema.sql
```

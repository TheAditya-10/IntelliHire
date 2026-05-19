import os

from dotenv import load_dotenv

load_dotenv()


def _require_env(name: str) -> str:
	value = os.getenv(name, "").strip()
	if not value:
		raise RuntimeError(f"Missing required environment variable: {name}")
	return value


def _normalize_database_url(raw_url: str) -> str:
	if raw_url.startswith("postgres://"):
		raw_url = raw_url.replace("postgres://", "postgresql://", 1)
	if raw_url.startswith("postgresql://") and "sslmode=" not in raw_url:
		separator = "&" if "?" in raw_url else "?"
		raw_url = f"{raw_url}{separator}sslmode=require"
	return raw_url


DATABASE_URL = _normalize_database_url(_require_env("DATABASE_URL"))
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv("SECRET_KEY", "").strip()
if not SECRET_KEY:
	if os.getenv("FLASK_ENV") == "production":
		raise RuntimeError("SECRET_KEY is required in production")
	SECRET_KEY = "dev-secret-key"
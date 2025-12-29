import os

class SettingsError(RuntimeError):
    pass

def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise SettingsError(f"Missing required env var: {name}")
    return value

def load_settings():
    env = require_env("APP_ENV")

    if env not in {"development", "staging", "production"}:
        raise SettingsError(f"Invalid APP_ENV: {env}")

    return {
        "env": env,
        "api_key": require_env("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
    }

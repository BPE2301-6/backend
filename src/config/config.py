from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

BASE_DIR = Path(__file__).parent.parent.parent
TOML_SETTINGS_PATH = BASE_DIR / "config.toml"


class App(BaseModel):
    """Основные параметры приложения."""

    host: str = Field(default="0.0.0.0", description="Хост, на котором запускается приложение.")
    port: int = Field(default=8000, description="Порт, на котором слушает FastAPI.")
    reload: bool = Field(default=True, description="Автоматическая перезагрузка при изменении кода.")
    debug: bool = Field(default=True, description="Режим отладки (больше логов и трассировка).")


class Database(BaseModel):
    """Параметры подключения к PostgreSQL."""

    postgres_username: str = Field(default="postgres", description="Имя пользователя PostgreSQL.")
    postgres_password: str = Field(default="postgres", description="Пароль пользователя PostgreSQL.")
    postgres_db: str = Field(default="postgres", description="Название базы данных.")
    postgres_host: str = Field(default="localhost", description="Хост PostgreSQL.")
    postgres_port: int = Field(default=5432, description="Порт PostgreSQL.")
    echo: bool = Field(default=False, description="Включить вывод SQL-запросов в лог.")

    @property
    def async_database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_username}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    app: App = App()
    database: Database = Database()

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ):
        return (
            init_settings,
            TomlConfigSettingsSource(settings_cls, TOML_SETTINGS_PATH),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )

settings = Config()

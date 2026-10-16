from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Student Management API BY SAPNA KUSHWAHA"
    database_url: str = "sqlite:///./students.db"

    class Config:
        env_file = ".env"


settings = Settings()

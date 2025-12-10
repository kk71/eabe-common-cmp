__all__ = [
    "backend_conf",
]

from rich import print
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class BackendConf(BaseSettings):
    """configurations for server-side"""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="ignore")
    debug: bool = Field(False, description="是否输出额外调试信息")
    prod_env: bool = Field(False, description="当前环境是否是生产环境")
    upload_path: str = Field(default="upload", description="上传文件所存放目录的位置")
    redis_host: str
    redis_port: int = 6379
    redis_user: str | None = None
    redis_password: str | None = None
    redis_db: int = 3
    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: str
    mysql_db: str
    jwt_key: str = "332c4df136c901318124407d4e6c2f64a7fc3fd43e7ea6c7286a8a8412540f11"
    jwt_timeout: int = Field(default=60*60*24*3, description="token失效时间秒")

    @classmethod
    def init(cls):
        global backend_conf
        if not backend_conf:
            backend_conf = cls()
            print(backend_conf)


backend_conf: BackendConf = None

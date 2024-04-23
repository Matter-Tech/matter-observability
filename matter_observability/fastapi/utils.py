from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from matter_observability.config import Config
from matter_observability.exceptions import MisConfigurationError

from .request_id import process_request_id


def configure_middleware(app: FastAPI, skip_paths: list[str] | None = None) -> None:
    metrics_path = "/internal/metrics"

    app.middleware("http")(process_request_id)

    if Config.ENABLE_METRICS:
        if bool(Config.INSTANCE_NAME) is False:
            raise MisConfigurationError("Environment variable: INSTANCE_NAME is not valid")

        Instrumentator().instrument(app=app).expose(app=app, endpoint=metrics_path)

import os


class Config:
    ENABLE_METRICS = os.getenv("ENABLE_METRICS", "true").lower() == "true"
    SERVER_LOG_LEVEL = os.getenv("SERVER_LOG_LEVEL", "info")
    PROMETHEUS_PUSH_GATEWAY_HOST = os.getenv("PROMETHEUS_PUSH_GATEWAY_HOST")
    INSTANCE_NAME = os.environ["INSTANCE_NAME"]

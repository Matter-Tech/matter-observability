import pytest
from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware

from matter_observability.exceptions import MisConfigurationError
from matter_observability.fastapi import configure_middleware


def test_configure_middleware_throws_exception_if_enable_metrics_is_not_set(mocker):
    mocker.patch("matter_observability.config.Config.INSTANCE_NAME", None)
    with pytest.raises(MisConfigurationError):
        configure_middleware(FastAPI())


def test_configure_middlewares_does_not_add_prometheus_middleware_if_enable_metrics_is_not_set(mocker):
    mocker.patch("matter_observability.config.Config.ENABLE_METRICS", False)

    app = FastAPI()
    app.add_middleware = mocker.Mock()

    configure_middleware(app)

    app.add_middleware.assert_called_once()


def test_configure_middlewares_happy_path(mocker):
    app = FastAPI()
    app.add_middleware = mocker.Mock()

    configure_middleware(app)

    app.add_middleware.assert_called_with(
        PrometheusMiddleware, app_name="observability_instance", group_paths=True, skip_paths=["/stats/prometheus"]
    )

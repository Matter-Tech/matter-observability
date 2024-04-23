from unittest.mock import Mock

from fastapi import FastAPI
from pytest_mock import MockerFixture

from matter_observability.fastapi import configure_middleware


def test_configure_middlewares_does_not_add_prometheus_middleware_if_enable_metrics_is_not_set(mocker: MockerFixture):
    mocker.patch("matter_observability.config.Config.ENABLE_METRICS", False)

    app = FastAPI()
    app.add_middleware = mocker.Mock()

    configure_middleware(app)

    app.add_middleware.assert_called_once()


def test_configure_middlewares_happy_path(mocker: MockerFixture):
    app = FastAPI()
    mocker.patch.object(FastAPI, "add_middleware")
    instrumentator_mock = Mock
    mocker.patch(f"{configure_middleware.__module__}.Instrumentator", return_value=instrumentator_mock)
    instrumentator_mock.instrument = Mock(return_value=instrumentator_mock)
    instrumentator_mock.expose = Mock(return_value=instrumentator_mock)

    configure_middleware(app)

    instrumentator_mock.instrument.assert_called_once_with(app=app)
    instrumentator_mock.expose.assert_called_once_with(app=app, endpoint="/internal/metrics")

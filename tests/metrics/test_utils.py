from unittest.mock import ANY

import pytest

from matter_observability.exceptions import MisConfigurationError
from matter_observability.metrics.utils import publish_metrics


def test_publish_metrics_throws_exception_if_push_gateway_host_is_not_set(mocker):
    mocker.patch("matter_observability.config.Config.PROMETHEUS_PUSH_GATEWAY_HOST", None)

    with pytest.raises(MisConfigurationError):
        publish_metrics()


def test_publish_metrics_does_not_call_publishing_method_if_metrics_are_not_enabled(mocker):
    mocker.patch("matter_observability.config.Config.ENABLE_METRICS", False)
    push_to_gateway_mocked = mocker.patch("matter_observability.metrics.utils.push_to_gateway")

    publish_metrics()

    push_to_gateway_mocked.assert_not_called()


def test_publish_metrics_happy_path(mocker):
    push_to_gateway_mocked = mocker.patch("matter_observability.metrics.utils.push_to_gateway")

    publish_metrics()

    push_to_gateway_mocked.assert_called_with(
        "localhost:9091",
        job="batch_observability_instance",
        registry=ANY,
        timeout=1,
    )

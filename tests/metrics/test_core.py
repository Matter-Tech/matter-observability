import time
import uuid

from matter_observability.metrics import (
    COUNTER_CUSTOM,
    GAUGE_CUSTOM,
    GAUGE_PROCESSING_TIME,
    LabeledCounter,
    LabeledGauge,
    LabeledGaugeDuration,
)


def test_gauge_should_be_set():
    labeled_gauge = LabeledGauge(metric=GAUGE_CUSTOM, label="test")
    labeled_gauge.set(10.0)
    assert labeled_gauge.metric._metrics[("test",)]._value._value == 10.0


def test_gauge_should_measure_duration():
    labeled_gauge = LabeledGaugeDuration(metric=GAUGE_PROCESSING_TIME, label="test")
    labeled_gauge.start()
    time.sleep(2)
    labeled_gauge.stop()
    assert round(labeled_gauge.metric._metrics[("test",)]._value._value) == 2


def test_counter_should_count():
    test_label = f"test_{uuid.uuid4()}"
    labeled_counter = LabeledCounter(metric=COUNTER_CUSTOM, label=test_label)
    for i in range(10):
        labeled_counter.inc()
    assert labeled_counter.metric._metrics[(test_label,)]._value._value == 10

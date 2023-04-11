import time
import pytest
import uuid

from matter_observability.metrics import (
    LabeledGauge,
    LabeledGaugeDuration,
    LabeledCounter,
    GAUGE_CUSTOM,
    GAUGE_PROCESSING_TIME,
    COUNTER_CUSTOM,
    gauge_value,
    measure_processing_time,
    count_occurrence,
)


def test_should_set_gauge_value_sync():
    @gauge_value(label="test")
    def to_be_decorated(gauge):
        gauge.set(10.0)

    to_be_decorated()
    labeled_gauge = LabeledGauge(metric=GAUGE_CUSTOM, label="test")
    assert labeled_gauge.metric._metrics[("test",)]._value._value == 10.0


@pytest.mark.asyncio
async def test_should_set_gauge_value_async():
    @gauge_value(label="test")
    async def to_be_decorated(gauge):
        gauge.set(10.0)

    await to_be_decorated()
    labeled_gauge = LabeledGauge(metric=GAUGE_CUSTOM, label="test")
    assert labeled_gauge.metric._metrics[("test",)]._value._value == 10.0


def test_should_collect_duration_sync():
    @measure_processing_time(label="test")
    def to_be_decorated():
        time.sleep(1)

    to_be_decorated()
    labeled_gauge = LabeledGaugeDuration(metric=GAUGE_PROCESSING_TIME, label="test")
    assert round(labeled_gauge.metric._metrics[("test",)]._value._value) == 1


@pytest.mark.asyncio
async def test_should_collect_duration_async():
    @measure_processing_time(label="test")
    async def to_be_decorated():
        time.sleep(1)

    await to_be_decorated()
    labeled_gauge = LabeledGaugeDuration(metric=GAUGE_PROCESSING_TIME, label="test")
    assert round(labeled_gauge.metric._metrics[("test",)]._value._value) == 1


def test_should_count_occurrences_sync():
    test_label = f"test_{uuid.uuid4()}"

    @count_occurrence(label=test_label)
    def to_be_decorated():
        pass

    for i in range(10):
        to_be_decorated()

    labeled_counter = LabeledCounter(metric=COUNTER_CUSTOM, label=test_label)
    assert labeled_counter.metric._metrics[(test_label,)]._value._value == 10


@pytest.mark.asyncio
async def test_should_count_occurrences_async():
    test_label = f"test_{uuid.uuid4()}"

    @count_occurrence(label=test_label)
    async def to_be_decorated():
        pass

    for i in range(10):
        await to_be_decorated()

    labeled_counter = LabeledCounter(metric=COUNTER_CUSTOM, label=test_label)
    assert labeled_counter.metric._metrics[(test_label,)]._value._value == 10

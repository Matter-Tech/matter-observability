# matter-observability

**Table of Contents**

- [Installation](#installation)
- [License](./LICENSE)

## Background

The Matter observability library for Python is a powerful tool for developers looking to improve their observability in Kubernetes environments. Specifically designed to integrate with FastAPI applications, this library offers support for both endpoint and push-gateway integration with Prometheus, allowing developers to easily monitor the performance and behavior of their applications.

The library provides a range of logging and metrics functionality, giving developers granular visibility into the inner workings of their applications. With logging, developers can easily track and diagnose errors, warnings, and other issues, while metrics enable them to track performance metrics like response time, request volume, and error rates.

In addition to its powerful logging and metrics capabilities, the Python observability library is designed with scalability in mind. Its push-gateway integration allows developers to easily scale up their monitoring capabilities, while its endpoint integration offers a more lightweight option for smaller deployments.

Looking towards the future, the Python observability library is committed to expanding its functionality to include tracing, giving developers even more insight into the performance and behavior of their applications. Whether you're a seasoned developer or just getting started with observability in Kubernetes, this library offers a powerful and flexible solution for monitoring and debugging your FastAPI applications.


## Getting started

### Integrate from FastAPI:
```python
# app is a Fast API app
app = FastAPI(
    root_path=env.PATH_PREFIX,
)

from matter_observability.fastapi import add_middleware
add_middleware(app=app)
```


### Use for setting Custom Metrics:

Set a Gauge:
```python
from matter_observability.metrics import (
    LabeledGauge,
    GAUGE_CUSTOM,
)

labeled_gauge = LabeledGauge(metric=GAUGE_CUSTOM, label="your-metric-name")
labeled_gauge.set(10.0)
```

Measure Duration:
```python
from matter_observability.metrics import (
    LabeledGaugeDuration,
    GAUGE_PROCESSING_TIME,
)

labeled_gauge = LabeledGaugeDuration(metric=GAUGE_PROCESSING_TIME, label="test")
labeled_gauge.start()
# ... some operation
labeled_gauge.stop()
```

Set a Counter:
```python
from matter_observability.metrics import (
    LabeledCounter,
    COUNTER_CUSTOM,
)

labeled_counter = LabeledCounter(metric=COUNTER_CUSTOM, label="your-metric-name")
labeled_counter.inc()
```


### Use with Decorators:

Set a Gauge - Sync:
```python
from matter_observability.metrics import (
    gauge_value,
)

@gauge_value(label="your-metric-name")
def my_func(gauge):
    gauge.set(10.0)

my_func()
```

Set a Gauge - Async:
```python
from matter_observability.metrics import (
    gauge_value,
)

@gauge_value(label="your-metric-name")
async def my_func(gauge):
    gauge.set(10.0)

await my_func()
```

Measure Duration - Sync:
```python
from matter_observability.metrics import (
    measure_processing_time,
)

@measure_processing_time(label="your-metric-name")
def my_func():
    time.sleep(1)

my_func()
```

Measure Duration - Async:
```python
from matter_observability.metrics import (
    measure_processing_time,
)
@measure_processing_time(label="test")
async def my_func():
    time.sleep(1)

await my_func()
```

Set a Counter - Sync:
```python
from matter_observability.metrics import (
    count_occurrence,
)

@count_occurrence(label="your-metric-name")
def my_func():
    pass

my_func()
```

Set a Counter - Async:
```python
from matter_observability.metrics import (
    count_occurrence,
)

@count_occurrence(label="your-metric-name")
async def my_func():
    pass

await my_func()
```


## Installation

Install the Library:
```console
pip install matter-observability
```

Make sure that you have set the following ENV values:
```env
SERVER_LOG_LEVEL=debug
PROMETHEUS_PUSH_GATEWAY_HOST=localhost
INSTANCE_NAME=observability_instance
ENABLE_METRICS=true
```
The last one is required for the API metrics endpoint to be exposed - they are not enabled by default!


## Contributing

Make sure you have all supported python versions installed in your machine:

* 3.10
* 3.11
* 3.12

### Install hatch in your system

```https://hatch.pypa.io/latest/install/```

### Create the environment

```console
hatch env create
```

### Locate the new environment

```console
hatch env find default
```

Do your changes...

### Run the tests

```console
hatch run test
```

The command above will run the tests against all supported python versions
installed in your machine. For testing in other operating system you may use the
configured CI in github. 

### Bump a new version

In general, you just need to execute:

```console
hatch version
```

This command will update the minor version. i.e.:
No breaking changes and new feature has been added

We are using [semantic version](https://semver.org/), if you are doing a bug fix:

```console
hatch version fix
```

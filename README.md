# matter-observability

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Getting started

TODO


## Installation

```console
pip install matter-observability
```

## Contributing

Make sure you have all supported python versions installed in your machine:

* 3.9
* 3.10
* 3.11

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

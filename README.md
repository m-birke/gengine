# gengine

|     |     |
| --- | --- |
| Version | [![PyPI - Version](https://img.shields.io/pypi/v/gengine.svg)](https://pypi.org/project/gengine) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gengine.svg)](https://pypi.org/project/gengine) |
| Project | ![GitHub License](https://img.shields.io/github/license/m-birke/gengine) ![PyPI - Status](https://img.shields.io/pypi/status/gengine) ![PyPI - Format](https://img.shields.io/pypi/format/gengine) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/gengine) |
| CI | ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/m-birke/gengine/static-code-check.yml) |
| Code | ![PyPI - Types](https://img.shields.io/pypi/types/gengine) [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/) [![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |

-----

Engine for piping generators

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

*gengine* (short for *generator engine*) is a pipeline or workflow engine for iterating over generators within a pipe and passing the output to the following generators.

This makes it a perfect fit for pipeline oriented approaches where you don't want to write the iteration logic manually.

## Installation

```console
pip install gengine
```

## Usage

From a technical perspective, a gengine pipeline is just an ordered list of callables. Each callable implements a generator pattern (`yield`) or simply returns an output (`return`).
*gengine* iterates over **all** outputs of **each callable** in the list and makes sure that every output is forwarded through the whole pipeline.
`NoneType` is ignored and not forwarded (this is the reason why it is mandatory to pass an input to `GenGine.run`, even if the first callable doesn't use it).
Each callable must accept exactly one parameter.

```python
from gengine import GenGine

def my_gen(_inp):
    for j in range(10):
        yield j

def my_add(inp):
    return inp+2

def my_mul(inp):
    for i in range(3):
        yield inp*i

def my_filter(inp):
    if inp%2 == 0:
        return None
    else:
        return inp

g = GenGine([my_gen, my_add, my_mul, my_filter])

for el in g.run(1):
    print(el)
```

## License

`gengine` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

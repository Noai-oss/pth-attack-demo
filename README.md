# dot-pth-attack

> [!NOTE]
> Build systems: **setuptools** | [`Hatchling`](https://github.com/Noai-oss/dot-pth-attack/tree/hatch)

A minimal demo showing how a Python package can automatically install a `.pth` file.

## Usage

```bash
uv sync
uv run python
```

If `attach success!` is printed, `attack.pth` was installed and loaded by Python.

## How it works

`setup.py` customizes setuptools build commands to include `attack.pth` in sdists, wheels, and editable wheels.

## Note

For security research and learning only. Do not use in unauthorized environments.

# pth-attack-demo

> [!NOTE]
> Build systems: [`setuptools`](https://github.com/Noai-oss/pth-attack-demo/tree/main) | **Hatchling**

A minimal demo showing how a Python package can automatically install a `.pth` file.

## Usage

```bash
uv sync
uv run python
```

If `attach success!` is printed, `attack.pth` was installed and loaded by Python.

## How it works

```toml
[tool.hatch.build.targets.wheel.force-include]
"attack.pth" = "attack.pth"
```

`force-include` maps `attack.pth` to the wheel root, so it installs to `site-packages/attack.pth`.

`artifacts` includes extra build files like `_version.py`; it does not set file locations inside the wheel.

## Note

For security research and learning only. Do not use in unauthorized environments.

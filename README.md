# Shotgrid Stubs
This rez package generates shotgrid stubs using MyPy and makes developing shotgrid apps a little more convenient.

## Dependencies
```
rez pip --install mypy
```

## Building
This package uses rezs custom build system feature to build the stubs with stubgen. so building is simple.
```
rez build -i
```

## Usage
Once you are in a resolved environment the pyi files are in the pythonpath so they can be imported as follows.

```python
import typing
if typing.TYPE_CHECKING:
    import tk_multi_publish2
```

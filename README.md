# Shotgrid Stubs
This rez package generates shotgrid stubs using MyPy enabling much richer IDE completions.

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

name = "shotgrid_stubs"
version = "0.0.0"

requires = ["mypy", "python-3"]

build_command = "python3 {root}/build.py"


def commands():
    env.PYTHONPATH.append("{root}/stubs")

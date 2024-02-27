name = "shotgrid_stubs"
version = "0.0.0"

requires = ["python-3"]
build_requires=["mypy"]

build_command = [
        "python3",
        "{root}/build.py",
        "--source", "tk-core", "python/tank", "out/tank",
        "--source", "tk-multi-publish2", "python/tk_multi_publish2", "out/python/tk_multi_publish2"
]


def commands():
    env.PYTHONPATH.append("{root}/stubs")

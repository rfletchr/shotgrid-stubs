import shutil
import sys
import os
import subprocess
import typing


def get_git_url(repo):
    return f"https://github.com/shotgunsoftware/{repo}"


def git_clone(url, directory):
    print(f"Pulling: {url}")
    cmd = ["git", "clone", url, directory]
    subprocess.check_call(cmd)

def stubgen(directory):
    print(f"Generating stubs for: {directory}")
    cmd = ["stubgen", directory]
    subprocess.check_call(cmd)


class Args(typing.NamedTuple):
    repo:str
    source_rel: str 
    paths: typing.List[str]


repo_names = [
        Args("tk-core", "python/tank", ["out/tank"]),
        Args("tk-multi-publish2", "python/tk_multi_publish2", ["out/python/tk_multi_publish2"]),
]

cwd = os.getcwd()
install = os.environ.get("REZ_BUILD_INSTALL") == "1"
rez_install_path = os.environ.get("REZ_BUILD_INSTALL_PATH")

for args in repo_names:
    path = os.path.join(cwd, args.repo)
    url = get_git_url(args.repo)
    if not os.path.exists(path):
        git_clone(url, path)
    
    stubgen(os.path.join(path, args.source_rel))

    if not install:
        continue

    for relpath in args.paths:
        source_path = os.path.join(cwd, relpath)
        install_path = os.path.join(rez_install_path, os.path.basename(relpath))
        print(f"Installing: {source_path} -> {install_path}")
        if os.path.exists(install_path):
            shutil.rmtree(install_path)
        shutil.copytree(source_path, install_path)


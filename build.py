import shutil
import sys
import os
import subprocess
import typing
import argparse



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



def build(repo, source_rel, target_rels):
    cwd = os.getcwd()
    install = os.environ.get("REZ_BUILD_INSTALL") == "1"
    rez_install_path = os.environ.get("REZ_BUILD_INSTALL_PATH")

    path = os.path.join(cwd, repo)
    url = get_git_url(repo)
    if not os.path.exists(path):
        git_clone(url, path)
    
    stubgen(os.path.join(path, source_rel))

    if not install:
        return

    for relpath in target_rels:
        source_path = os.path.join(cwd, relpath)
        install_path = os.path.join(rez_install_path, os.path.basename(relpath))
        print(f"Installing: {source_path} -> {install_path}")
        if os.path.exists(install_path):
            shutil.rmtree(install_path)
        shutil.copytree(source_path, install_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", nargs="+", dest="sources", action="append")

    args = parser.parse_args()
    print(args)
    for source in args.sources:
        print(source)
        repo = source[0]
        source_rel = source[1]
        target_rels = source[2:]
        build(repo, source_rel, target_rels)


if __name__ == "__main__":
    main()

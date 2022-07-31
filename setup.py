import os
from setuptools import find_packages, setup


files = {
    "long_description": "README.md",
    "requirements": "requirements.txt",
    "version": "VERSION",
    "license": "LICENSE",
}

param = {}

for key in files:
    try:
        with open(files[key]) as file:
            param[key] = file.read()
    except(OSError, IOError) as exc:
        param[key] = ""

param["name_project"] = os.path.basename(os.getcwd())

setup(
    name=param["name_project"],
    description="TemplateFPP app",
    packages=find_packages(exclude=("test", "venv",  "docs")),
    install_requires=param["requirements"],
    #entry_points={"console_scripts": [f"{param['name_project']} = {param['name_project']}.app:main"]},
    **param
)
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."  ## present in requirement.txt

def get_requirements(file_path: str) -> List[str]:
    '''
    This function is used to return all requirements for this project
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        ## read every requirement line by line and install it

        # strip() removes all whitespace/newlines (\n, \r\n, spaces, tabs)
        # safer than replace("\n", "") because different OS have different line endings
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  ## to ignore -e . from the requirement.txt

    return requirements

setup(
    name="ml_project_1",
    version="0.0.1",
    author="Sourav Yogi",
    author_email="souravyogi00@gmail.com",
    packages=find_packages(),   ## automatically finds all packages (__init__.py files)
    install_requires=get_requirements("requirements.txt"),  ## install requirements dynamically
)

#!/usr/bin/env python3
from setuptools import setup, find_packages, Extension

with open("README.md", "r") as fh:
    project_description = fh.read()

    """Block 1 - Trigger platform specific wheel
    """
# try:
#     from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
#     class bdist_wheel(_bdist_wheel):
#         def finalize_options(self):
#             _bdist_wheel.finalize_options(self)
#             self.root_is_pure = False
# except ImportError:
#     bdist_wheel = None


setup(
    name            =   "val-wrapper",
    version         =   "0.3",
    author          =   "Anubhav Singh",
    author_email    =   "anubhav.singh.er@pm.me",
    description     =   "plan validation toolkit",
    long_description=   project_description,
    long_description_content_type='text/markdown',
    url             =   "https://github.com/LAPKT-dev/val-wrapper",
    packages        =   find_packages('package'),  
    package_dir     =   {'': 'package'},  
    classifiers     =   [
                        "Programming Language :: Python :: 3",
                        "License :: OSI Approved :: BSD License",
                        "Operating System :: Microsoft :: Windows",
                        "Operating System :: POSIX :: Linux",
                        "Operating System :: MacOS"
                        ],
    python_requires =   '>=3.7',
    install_requires=   [],
    extras_require  =   {},
    scripts         =   ['package/scripts/validate.py', ],
    include_package_data = True,

    # cmdclass={'bdist_wheel': bdist_wheel}, # Part of Block 1

    ## Block 2 - An alternative method to trigger platform specific wheel
    ##         - Has issues on windows   
    # ext_modules=[
    #     Extension(
    #         name='my.dummy.module',
    #         sources=[]
    #     )
    # ]
)

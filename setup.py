from __future__ import absolute_import
import os
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sagemaker_sklearn_container',
    version='2.0',
    description='Open source library for creating SciKit-Learn containers to run on Amazon SageMaker.',

    packages=find_packages(where='src', exclude=('test',)),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],

    long_description=read('README.md'),
    author='Amazon Web Services',
    license='Apache License 2.0',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    install_requires=read("requirements.txt"),

    extras_require={
        'test': read("test-requirements.txt")
    },

    entry_points={
        'console_scripts': 'serve=sagemaker_sklearn_container.serving:serving_entrypoint'
    },

    python_requires='>=3.6',
)

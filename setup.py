from setuptools import setup, find_packages

import io
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(this_directory, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='EPL-data-boardxx',
    version='0.0.4',
    packages=find_packages(),
    url='https://github.com/Kshitiz-Mhto/EPL-data-board',
    license='https://www.apache.org/licenses/LICENSE-2.0',
    license_files=["LICENSE"],
    author='Ibceberg',
    author_email='ibergx00@gmail.com',
    description='Pthon Wrapper',
    long_description="lala is here",
    long_description_content_type='text/markdown',

    tests_require=[],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7']
)
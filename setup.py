from setuptools import setup, find_packages

setup(
    name="behave_odoo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "behave",
    ],
    author="Coopdevs",
    author_email="pelayo.garcia@coopdevs.org",
    description="Helper functions for simplifying the process of writing behave tests for Odoo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/coopdevs/behave_odoo",
    license="AGPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

"""Lambda function setuptools entry point."""

from setuptools import setup, find_packages

setup(
    name="humilis-kinesis-processor-lambda",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    # We often need the latest version of boto3 so we include it as a req
    install_requires=[
        "boto3==1.17.15",
        "raven==6.10.0",
        "contextlib2==0.6.0",
        "lambdautils==1.6.2",
        "werkzeug==1.0.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6"],
    zip_safe=False
)

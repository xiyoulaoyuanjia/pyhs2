from setuptools import setup

setup(
    name='pyhs2',
    version='0.4.1',
    author='Brad Ruderman',
    author_email='bradruderman@gmail.com',
    packages=['pyhs2', 'pyhs2/cloudera', 'pyhs2/TCLIService', 'pyhs2/TCLIServiceTornado'],
    url='https://github.com/BradRuderman/pyhs2',
    license='LICENSE.txt',
    description='Python Hive Server 2 Client Driver',
    long_description=open('README.md').read(),
    install_requires=[
        "sasl",
        "thrift",
        "tornado",
    ],
    test_suite='pyhs2.test',
    tests_require=["mock"]

)


from setuptools import setup, find_packages

install_requires = [
        "predix",
    ]

setup_requires = [
    ]

long_description = 'See GitHub README.rst for more details.'
with open('README.rst') as file:
   long_description = file.read()

setup(
        name="predixpy-examples",
        version="0.0.3",
        author="Jayson DeLancey",
        author_email="jayson.delancey@ge.com",
        description="Utilities Using Predix Python SDK",
        long_description=long_description,
        setup_requires=setup_requires,
        install_requires=install_requires,
        package_data={
            '': ['*.md', '*.rst'],
            },
        packages=find_packages(exclude=['test', 'test.*']),
        test_suite="test.unit",
        entry_points={
            'console_scripts': [
                ]
        },
        tests_require=[],
        keywords=['predix', 'ge', 'asset', 'analytics'],
        url="https://github.com/PredixDev/predixpy-examples",
        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approved :: BSD License',
            'Development Status :: 3 - Alpha']
    )

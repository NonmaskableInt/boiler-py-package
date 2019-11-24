from setuptools import setup, find_namespace_packages

setup(
    name="",
    version="0.0.1",
    packages=find_namespace_packages(include=['forex.*']),
    author="Chris Lawcock",
    author_email="lawcockc@gmail.com",
    description="A python implementation for working with ",
    keywords=" example tests etc",
    # url="http://example.com/HelloWorld/",   # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],    
    # entry_points={
    #     'console_scripts': [
    #         'foo = my_package.some_module:main_func',
    #         'bar = other_module:some_func',
    #     ],
    #     'gui_scripts': [
    #         'baz = my_package_gui:start_func',
    #     ]
    # }  
    # install_requires=[""],  
)

# Before you begin, make sure you have the latest versions of setuptools and wheel:

# python3 -m pip install --user --upgrade setuptools wheel
# To build a setuptools project, run this command from the same directory where setup.py is located:

# python3 setup.py sdist bdist_wheel
# This will generate distribution archives in the dist directory.

# Before you upload the generated archives make sure you’re registered on https://test.pypi.org/account/register/. You will also need to verify your email to be able to upload any packages. You should install twine to be able to upload packages:

# python3 -m pip install --user --upgrade setuptools wheel
# Now, to upload these archives, run:

# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# To install your newly uploaded package example_pkg, you can use pip:

# python3 -m pip install --index-url https://test.pypi.org/simple/ example_pkg
# If you have issues at any point, please refer to Packaging project tutorials for clarification.
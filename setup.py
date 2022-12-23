from setuptools import setup, find_packages

setup(
    name='mediainfoparser',
    version='0.1.1',
    url='https://github.com/jirih/mediainfoparser',
    packages=find_packages(),
    license='GPLv3',
    author='jirih',
    author_email='',
    description='Parser of mediainfo command output',
    long_description='Parser of mediainfo command output',
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'mediainfoparser = mediainfoparser.mediainfoparser:main'
        ]
    }, install_requires=[

    ],

)

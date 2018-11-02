import codecs

import setuptools

from whitespacelint import __version__ as version

setuptools.setup(
    name='whitespacelint',
    version=version,
    description='Linting tool for whitespace',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    keywords='lint',
    author='Bendik',
    author_email='bro.dev@gmail.com',
    url='https://github.com/bendikro/whitespacelint',
    license='MIT',
    test_suite="tests",
    packages=['whitespacelint'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'whitespacelint = whitespacelint.whitespacelint:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

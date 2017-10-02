import codecs

import setuptools

from bashlint import __version__ as version


setuptools.setup(
    name='bashlint',
    version=version,
    description='Bash linting tool',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    keywords='bash',
    author='Stanislav Kudriashev',
    author_email='stas.kudriashev@gmail.com',
    url='https://github.com/skudriashev/bashlint',
    download_url='https://github.com/skudriashev/bashlint/tarball/0.1.0',
    license='MIT',
    test_suite="tests",
    packages=['bashlint'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'bashlint = bashlint.bashlint:main',
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

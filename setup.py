from setuptools import setup

import os


# Installed name used for various commands (both script and setuptools).
command_name = os.environ.get('CIU_ALT_NAME') or 'caniusepypy'

with open('README_PyPI.rst') as file:
    long_description = file.read()

with open('dev_requirements.txt') as file:
    tests_require = [dep.strip() for dep in file.readlines()]

setup(name='caniusepypy',
      version='1.0.0',
      description='Determine what projects are blocking you from porting to PyPy',
      long_description=long_description,
      author='Alex Stapleton',
      author_email='alex@lyst.com',
      url='https://github.com/public/caniusepypy',
      packages=['caniusepypy', 'caniusepypy.test'],
      include_package_data=True,
      install_requires=['distlib', 'setuptools', 'pip',  # Input flexibility
                        'argparse', 'futures'],  # Functionality
      tests_require=tests_require,  # Testing, external due to Travis
      test_suite='caniusepypy.test',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      entry_points={
          'console_scripts': [
              '{0} = caniusepypy.__main__:main'.format(command_name),
          ],
          'distutils.commands': [
              '{0} = caniusepypy.command:Command'.format(command_name),
          ],
      },
      zip_safe=True,
)

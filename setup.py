# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from imrpyml2019.init import train
import distutils.cmd
import distutils.command.build
import sys

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

class PrepareCommand(distutils.cmd.Command):
    description = 'Pre-compile model for the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        train()


class BuildPyCommand(distutils.command.build.build):
  """Make sure to build model before anything."""

  def run(self):
    self.run_command('prepare')
    distutils.command.build.build.run(self)

# From https://stackoverflow.com/questions/45150304/how-to-force-a-python-wheel-to-be-platform-specific-when-building-it
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

        def get_tag(self):
            python, abi, plat = _bdist_wheel.get_tag(self)
            # We don't contain any python source
            python, abi = 'py' + str(sys.version_info.major) + str(sys.version_info.minor), 'none'
            return python, abi, plat

except ImportError:
    bdist_wheel = None

setup(
    name='imrpyml2019',
    version='0.0.2',
    description='Sample package for creating a multi-platform package for Keras pre-compiled model',
    long_description=readme,
    author='Ibrahim Umar',
    author_email='ibrahim.umar@hi.no',
    url='https://github.com/iambaim/python-keras-ml-ci',
    license=license,
    packages=['imrpyml2019'],
    include_package_data=True,
    install_requires=[
        "tensorflow",
        "numpy",
        "matplotlib",
        "pillow"
    ],
    cmdclass={
        'bdist_wheel': bdist_wheel,
        'prepare': PrepareCommand,
        'build': BuildPyCommand
    },
)


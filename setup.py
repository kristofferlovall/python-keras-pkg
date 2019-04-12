# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from imrpyml2019.init import train
import distutils.cmd
import distutils.command.build

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

setup(
    name='imrpyml2019',
    version='0.0.1',
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
        'prepare': PrepareCommand,
        'build': BuildPyCommand
    },
)


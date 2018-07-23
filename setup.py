from setuptools import setup

setup(
    name='fleck',
    version='0.0.1',
    description='Falling sand physics sandbox game.',
    packages=['fleck_game'],
    setup_requires=['Cython==0.28.3'],
    install_requires=['kivy', 'numpy'],
    scripts=['bin/fleck-game'],
    include_package_data=True
)

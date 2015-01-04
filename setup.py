from distutils.core import setup

setup(
    name='mist-monitor',
    version='1.0.0',
    packages=['mist', 'mist_monitor'],
    url='https://www.github.com/barakm/mist-monitor',
    license='',
    author='barakme',
    author_email='barakme@gmail.com',
    description='mist monitoring utilities',
    install_requires=[
        'mist.client'
    ]
)

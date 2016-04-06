from setuptools import setup

setup(
    name='chatbot',
    version='1',
    py_modules=['chatbot'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        chat=chatbot:cli
    ''',
)

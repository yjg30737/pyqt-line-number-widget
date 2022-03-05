from setuptools import setup, find_packages

setup(
    name='pyqt-line-number-widget',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='QWidget which shows line numbers of QTextBrowser or QTextEdit',
    url='https://github.com/yjg30737/pyqt-line-number-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)
from setuptools import setup, find_packages

setup(
    name='amazon-monitor',
    version='1.0.0',
    author='Dr. H',
    author_email='han@yonro.co.jp',
    description='Monitor Amazon products and send email/twitter notification when available',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
        'tweepy==3.10.0',
    ],
    entry_points={
        'console_scripts': [
            'amazon-monitor=amazon_monitor:main',
        ],
    },
)

import setuptools

setuptools.setup(
    name="snap-watchdog-tricks",
    version='1.2.4',
    license="MIT",

    author="Martin Moss",
    author_email="helpteam@getasnap.com",
    url="https://github.com/snap-labs/snap-watchdog-tricks",

    description="Some tricks for watchdog (Python file system monitoring tool), including CheckBeforeAutoRestart",
    long_description=open("README.md").read(),
    keywords=["watchdog", "watcher", "tricks"],
    classifiers=[
            "Environment :: Console",
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Environment :: Other Environment",
            "Topic :: Utilities",
            "Topic :: System :: Monitoring",
            "Topic :: System :: Filesystems",
    ],
    install_requires=[
        'watchdog[watchmedo]==1.0.2',
        # 'watchdog_tricks@git+https://github.com/snap-labs/watchdog-tricks.git'
        'watchdog_tricks@https://github.com/snap-labs/watchdog-tricks/archive/v0.1.4.zip'
    ],
    packages=['snap_watchdog_tricks'],
)

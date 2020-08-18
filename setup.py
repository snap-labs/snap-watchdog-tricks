import setuptools

setuptools.setup(
    name="snap-watchdog-tricks",
    version='1.1.1',
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
        'watchdog[watchmedo]==0.10.3',
        # 'watchdog_tricks@git+https://github.com/snap-labs/watchdog-tricks.git'
        'watchdog_tricks@git+https://github.com/snap-labs/watchdog-tricks/tarball/v0.1.3#egg=watchdog-tricks'
    ],
    packages=['snap_watchdog_tricks'],
)

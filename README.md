watchdog-tricks
===============

This package includes several useful `Trick` for `watchdog` (Python API for monitoring file system events, https://github.com/gorakhargosh/watchdog).

Tricks could be running in standalone mode or combined via a configuration file. They will perform specific tasks upon file change event.

- CheckBeforeAutoRestartTrick: Provided a check process exits successfully Restart a process on source code changes

Configuration File - trick.yaml
-------------------------------
The true power of watchdog tricks is shown via configuration files, which could combine different tricks together and give you a fully automated development and building system.

Put the configuration file to the root directory that needs to be monitored. Assume the filename is `tricks.yaml`. To run watchdog with this configuration file

    $ watchmedo tricks tricks.yaml

API Documentation
-----------------
An example to restart gunicorn web servers on python source code changes

    tricks:
    - snap_watchdog_tricks.tricks.CheckBeforeAutoRestartTrick:
        patterns: ["*.py"]
        command: "celery -A config worker -l DEBUG -E"
		check_command: "./manage.py check"
        wait_for_process: true

Installation
------------

Install directly from github.com

    $ pip install git+git://github.com/snap-labs/snap-watchdog-tricks.git

Or clone this repository and run

	$ python setup.py install

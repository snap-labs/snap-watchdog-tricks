import os
import time
import signal
import subprocess

# Third party libraries
from watchdog.utils import echo
from watchdog_tricks.batch import BatchTrick


class CheckBeforeAutoRestartTrick(BatchTrick):

    """Starts a long-running subprocess and restarts it on matched events.

    The command parameter is a list of command arguments, such as
    ['bin/myserver', '-c', 'etc/myconfig.ini'].

    Call start() after creating the Trick. Call stop() when stopping
    the process.
    """

    def __init__(self, command, check_command, patterns=None, ignore_patterns=None,
                 ignore_directories=False, stop_signal=signal.SIGINT,
                 kill_after=10):
        super(CheckBeforeAutoRestartTrick, self).__init__(
            patterns, ignore_patterns, ignore_directories)
        self.command = command
        self.check_command = check_command
        self.stop_signal = stop_signal
        self.kill_after = kill_after
        self.process = None

    def check(self):

        print("Calling check command - {0}".format(self.check_command)
        check = subprocess.run([self.check_command], capture_output=True)
        print("Completed\n{0}".format(check.stdout))
        print("Return code ", check)
        if check.returncode == 0:
            return 1
        else:
            return 0

    def start(self):
        self.process = subprocess.Popen(self.command, preexec_fn=os.setsid)

    def stop(self):
        if self.process is None:
            return
        try:
            os.killpg(os.getpgid(self.process.pid), self.stop_signal)
        except OSError:
            # Process is already gone
            pass
        else:
            kill_time = time.time() + self.kill_after
            while time.time() < kill_time:
                if self.process.poll() is not None:
                    break
                time.sleep(0.25)
            else:
                try:
                    os.killpg(os.getpgid(self.process.pid), 9)
                except OSError:
                    # Process is already gone
                    pass
        self.process = None

    @echo.echo
    def on_multiple_events(self, events):
        if self.check():
            self.stop()
            self.start()
        else:
            pass

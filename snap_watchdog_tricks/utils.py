from subprocess import Popen, PIPE


class StreamCaptureCommandOutput():

    def streamcapture(self, command):

        # print("[STREAMCAPTURE] Starting for {0}".format(command))
        with Popen(command, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='')  # process line here

        # print("[STREAMCAPTURE] Finished for {0}".format(command))
        if p.returncode != 0:
            return 0
        return 1

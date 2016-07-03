"""This module contains base clasess for danata readers"""

import subprocess

class DNTReader(object):
    def __init__(self):
        self.inputdata = None

    def runshcmd(self, cmd, input=None, **kwargs):
        """Run shell command and returns stdout, stderr, and return code.

        """
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, \
        stderr=subprocess.PIPE, shell=True, **kwargs)
        out, err = proc.communicate(input=input)
        return out, err, proc.returncode

    def packshcmd(self, argv):
        newargv = []
        for arg in argv:
            if not isinstance(arg, str):
                continue
            newarg = arg.strip()
            if newarg.find(' ') >= 0:
                newargv.append('"%s"'%newarg)
            else:
                newargv.append(newarg)
        return ' '.join(newargv)


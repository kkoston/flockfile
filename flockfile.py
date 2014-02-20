import fcntl
import os

class FlockFile:
    def __init__(self, fname):
        self.fname = fname
        if not os.path.exists(fname):
            f = open(fname, "w+")
            f.close()

    def acquire(self):
        self.f = open(self.fname, "r+")
        fcntl.flock(self.f, fcntl.LOCK_EX)
        self.f.write(repr(os.getpid()))
        self.f.flush()

    def release(self):
        self.f.truncate(0)
        self.f.flush()
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()
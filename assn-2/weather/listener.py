import os
import errno
import time

TERMINATE_MESSAGE = "<!#TERMINATE#!>"
FIFO = f"fifo/{os.getpid()}"

if os.path.exists('/fifo'):
    os.mkdir('/fifo')

try:
    os.mkfifo(FIFO, mode=0o600)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise


print(f"Starting Listner with PID: {os.getpid()}......")


try:
    while True:
        report = ""
        with open(FIFO, "r") as fifoFile:
            report = fifoFile.read()

        if not report:
            time.sleep(0.1)

        elif report == TERMINATE_MESSAGE:
            print("Broadcaster is closed!!")
            print(f"Shutting down listener {os.getpid()}")
            break
        else:
            print(f"Weather: {report}")

except KeyboardInterrupt:
    pass
except:
    os.unlink(FIFO)
    raise
finally:
    os.unlink(FIFO)
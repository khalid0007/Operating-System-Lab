import os
import errno
import time
from colors import wrapTextWithStyle

FIFO = 'callerRcvFifo'

try:
    os.mkfifo(FIFO, mode=0o600)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

HANGUP_MESSAGE = 'hang up'
buffersize = 11

while True:
    with open(FIFO, "r") as fifoFile:
        msg = fifoFile.read()

    if msg == HANGUP_MESSAGE:
        break


    print(f"{wrapTextWithStyle('Caller:', 'White', 'Red', 'bold')} {msg}".rjust(os.get_terminal_size().columns + buffersize + 2, ' '))

    msg = input(wrapTextWithStyle("Receiver:", 'White', 'Black', 'bold') + " ")

    with open(FIFO, "w") as fifoFile:
        fifoFile.write(msg)

    if msg == HANGUP_MESSAGE:
        break

# if os.path.exists(FIFO):
#     os.unlink(FIFO)


# print(type(os.get_terminal_size()))

# print(os.get_terminal_size().lines)
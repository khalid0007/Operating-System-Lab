import os
import errno
import subprocess

TERMINATE_MESSAGE = "<!#TERMINATE#!>"


def getAllFifo():
    findFifo = subprocess.Popen(
        ["find", "./fifo", "-type", "p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = findFifo.communicate()

    if not stderr:
        stdout = str(stdout.decode("utf-8"))
        fifos = list(
            filter(
                lambda x: len(x) > 0,
                map(lambda x: x.lstrip(".").lstrip("/"), stdout.split("\n")),
            )
        )

        return fifos
    else:
        return []


def broadcastToAll(mssg):
    fifos = getAllFifo()

    if not fifos:
        if mssg != TERMINATE_MESSAGE:
            print("No listener found!")
        return

    for fifo in fifos:
        with open(fifo, "w") as fifoFile:
            fifoFile.write(mssg)


print("Starting Weather Broadcaster...")

while True:
    weatherReport = input("Enter Weather Report: ")

    fifos = getAllFifo()

    if not fifos:
        print("No Listener detected!!")
        continue

    broadcastToAll(weatherReport)

    closingConditon = input("Do you want to close broadcaster (Y/N): ")

    if closingConditon.lower() == "y":
        broadcastToAll(TERMINATE_MESSAGE)
        print("Shutting down broadcaster......")
        break
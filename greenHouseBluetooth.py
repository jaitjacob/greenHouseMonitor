import bluetooth
import time
import os
import subprocess as sp


class bluetoothNotify:
    def findNearByDevices(self, macAdd):
        i=0
        while(i<5):
            print("Scanning...")
            nearbyDevices = bluetooth.discover_devices()

            for macAddress in nearbyDevices:
                print("Found device with mac-address: " + macAddress)
                if(str(macAddress) == macAdd):
                    print("Match anu keto")
            i = i+1



    def sliceMacAddress(self, macAddress):
        sliceStart = int(macAddress.rindex("("))
        sliceEnd = int(macAddress.rindex(")"))
        _ = ""

        for x in range(sliceStart+1, sliceEnd):
            _ = _+macAddress[x]

        return macAddress
#

    def listPairedDevices(self):
        p = sp.Popen(["bt-device", "--list"], stdin=sp.PIPE,
                     stdout=sp.PIPE, close_fds=True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()
        myphone = data.pop(1)
        myphone = myphone.decode()
        return myphone


if __name__ == "__main__":
    blue = bluetoothNotify()

    myPhone = blue.listPairedDevices()
    macAdddress = blue.sliceMacAddress(myPhone)
    print(macAdddress)
    blue.findNearByDevices(macAdddress)
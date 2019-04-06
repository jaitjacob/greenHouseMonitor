import bluetooth, time, os
import subprocess as sp

class bluetoothNotify:
    def findNearByDevices(self):
        print("Scanning...")
        nearbyDevices = bluetooth.discover_devices()

        for macAddress in nearbyDevices:
            print("Found device with mac-address: " + macAddress)

        print("Sleeping for 10 seconds.")
        time.sleep(10)

    def sliceMacAddress(self,macAddress):
        sliceStart = int(macAddress.rindex("("))
        sliceEnd = int(macAddress.rindex(")"))
        _=""
        
        for x in range(sliceStart+1,sliceEnd):
            _=_+macAddress[x]            

        return macAddress
#

    
    def listPairedDevices(self):
        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()
        myphone=data.pop(1)
        myphone=myphone.decode()
        macAddress = self.sliceMacAddress(myphone)
        return macAddress


if __name__ == "__main__":
    blue = bluetoothNotify()
    blue.findNearByDevices()
    blue.listPairedDevices()
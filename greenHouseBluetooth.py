import bluetooth, time, os
import subprocess as sp

class bluetoothNotify:
    def findNearByDevices(self):
            print("Scanning...")
            nearbyDevices = bluetooth.discover_devices()

            for macAddress in nearbyDevices:
                print("Found device with mac-address: " + macAddress)

    def sliceMacAddress(self,macAddress):
        sliceStart = int(macAddress.rindex("("))
        sliceEnd = int(macAddress.rindex(")"))
        
        
        print(sliceStart)
        print(sliceEnd)

        macAddress = macAddress.split(sliceStart,sliceEnd)
        print(macAddress)
        
#

    
    def listPairedDevices(self):
        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()
        print(data)
        myphone=data.pop(1)
        myphone=myphone.decode()
        self.sliceMacAddress(myphone)
        
if __name__ == "__main__":
    blue = bluetoothNotify()
    blue.findNearByDevices()
    blue.listPairedDevices()
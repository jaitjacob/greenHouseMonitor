import bluetooth, time, os
import subprocess as sp

class bluetoothNotify:
    def findNearByDevices(self):
            print("Scanning...")
            nearbyDevices = bluetooth.discover_devices()

            for macAddress in nearbyDevices:
                print("Found device with mac-address: " + macAddress)

            print("Sleeping for 5 seconds.")
            time.sleep(5)

    def listPairedDevices(self):
        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()
        print(data)
        myphone=str(data.pop(1))
        myphone.decode()
        print(myphone)
#
if __name__ == "__main__":
    blue = bluetoothNotify()
    blue.findNearByDevices()
    blue.listPairedDevices()
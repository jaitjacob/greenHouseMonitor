#!/usr/bin/env python3
import bluetooth
import time
import os
import subprocess as sp
import pushNotify, monitorAndNotify

class bluetoothNotify:
    def notifyCurrentStat(self):
        monitor = monitorAndNotify.monitor()
        h,t = monitor.getSensorData()
        message = "Current temperature is " + str(t) + " and humidity is " + str(h)
        pushNotify.send_notification_via_pushbullet("Bluetooth Alert",message)

    def findNearByDevices(self, macAdd):
        i=0
        while(i<5):
            print("Scanning...")
            nearbyDevices = bluetooth.discover_devices()

            for macAddress in nearbyDevices:
                if(str(macAddress) == macAdd):
                    self.notifyCurrentStat()
                    break
            i = i+1


    def sliceMacAddress(self, macAddress):
        sliceStart = int(macAddress.rindex("("))
        sliceEnd = int(macAddress.rindex(")"))
        _ = ""

        for x in range(sliceStart+1, sliceEnd):
            _ = _+macAddress[x]

        return _
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
    blue.findNearByDevices(macAdddress)
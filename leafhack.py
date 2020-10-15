#this is the leafhack program
import can

bus = can.Bus(interface='socketcan',channel='can0')

CAR = {"voltage": 372, "speed": 608, "tachometer": 1549}

def cellvoltage(SingleCanFrame, MyDB):
    #convert data
    #save to DB table 1
    print("cellvoltage called", SingleCanFrame)

def packcurrent(SingleCanFrame, MyDB):
    #convert data
    #save to DB table 2
    print("packcurrent called", SingleCanFrame)

def tachometer(SingleCanFrame, MyDB):
    #convert data
    #save to DB table 3
    print("tachometer called", SingleCanFrame)

def parse_data(can):
    SingleCanFrame = can.Message
    MyDB = 1
    print(SingleCanFrame.arbitration_id)

    if SingleCanFrame.arbitration_id == CAR["voltage"]: #car voltage
        cellvoltage(SingleCanFrame, MyDB)

    elif SingleCanFrame.arbitration_id == CAR["speed"]: #car speed
        packcurrent(SingleCanFrame, MyDB)

    elif SingleCanFrame.arbitration_id == CAR["tachometer"]:    #car tachometer
        tachometer(SingleCanFrame, MyDB)

    else:
        print("this is the else statement")
        #save to DB errorlog

notifier = can.Notifier(bus, [parse_data(can)])



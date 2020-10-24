#this is the leafhack program
import can
import struct

CAR = {"shifter position": 372,   #ID 0x174
    "speed": 852,                 #ID 0x354
    "tire pressure": 901,         #ID 0x385
    "outside temp": 1296          #ID 0x510
}

filters = [
    {"can_id": CAR["shifter position"], "can_mask": 0x7FF},
    {"can_id": CAR["speed"], "can_mask": 0x7FF},
    {"can_id": CAR["tire pressure"], "can_mask": 0x7FF},
    {"can_id": CAR["outside temp"], "can_mask": 0x7FF},
]

bus = can.interface.Bus(channel="can0", bustype="socketcan", can_filters=filters)

def shifterposition(SingleCanFrame, MyDB):

    dummy = struct.unpack('BBBBBBBB', SingleCanFrame.data)

    if dummy[3] == 170:           #0xAA
      shifter_status = "PARK"
    elif dummy[3] == 187:         #0xBB
      shifter_status = "DRIVE"
    elif dummy[3] == 153:         #0x99
      shifter_status == "REVERSE"
    else:
      shifter_status == "UNKNOWN"

    print("shifter:", shifter_status)
    #TODO log the shifter status to the log file

def speed(SingleCanFrame, MyDB):

    speed = struct.unpack('BBBBBBBB', SingleCanFrame.data)

    print("speed  :", speed[0])
    #TODO verify that this is the correct units
    #TODO log speed to the log file

def tirepressure(SingleCanFrame, MyDB):
    #convert data
    #save to DB table 3
    print("tirepre:", SingleCanFrame.data)

def outsidetemp(SingleCanFrame, MyDB):
    #convert data
    #save to DB table 4
    print("temp   :", SingleCanFrame.data)

def parse_data(can):
    SingleCanFrame = can
    MyDB = 1
    #print("Printing SingleCanFrame.arbitration_id:")
    #print(SingleCanFrame.arbitration_id)
    #print("Printing data:")
    #print(SingleCanFrame.data)
    #print(SingleCanFrame)

    #print("\033c", end="")

    if SingleCanFrame.arbitration_id == CAR["shifter position"]: #car's shifter position
        shifterposition(SingleCanFrame, MyDB)

    elif SingleCanFrame.arbitration_id == CAR["speed"]: #car speed
        speed(SingleCanFrame, MyDB)

    elif SingleCanFrame.arbitration_id == CAR["tire pressure"]: #tire pressure
        tirepressure(SingleCanFrame, MyDB)

    elif SingleCanFrame.arbitration_id == CAR["outside temp"]: #outside temp
        outsidetemp(SingleCanFrame, MyDB)

    #else:
        #print("this is the else statement")
        #save to DB errorlog

for msg in bus:
    parse_data(msg)




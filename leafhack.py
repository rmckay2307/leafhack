#this is the leafhack program
import can
import struct
import tkinter as tk

###################################################################################################
# DEFINE PARAMETERS

CAR = {"shifter position": 372,   #ID 0x174
    "speed": 640,                 #ID 0x280
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

##################################################################################################
# DEFINE GLOBAL VARIABLES

previous_speed = 0
previous_time = 0

#################################################################################################
# DEFINE FUNCTIONS

def shifterposition(SingleCanFrame):

    dummy = struct.unpack('BBBBBBBB', SingleCanFrame.data)

    if dummy[3] == 170:           #0xAA
      shifter_status = "PARK"
    elif dummy[3] == 187:         #0xBB
      shifter_status = "DRIVE"
    elif dummy[3] == 153:         #0x99
      shifter_status = "REVERSE"
    else:
      shifter_status = "UNKNOWN"

    print("shifter:", shifter_status)
    #TODO log the shifter status to the log file

def speed(SingleCanFrame):

    speed = struct.unpack('BBBBBBBB', SingleCanFrame.data)
    current_speed = speed[4] * .0062 #convert to MPH
    current_time = SingleCanFrame.timestamp

    global previous_speed
    global previous_time

    acceleration = (current_speed - previous_speed) / (current_time - previous_time)

    print("speed  :", speed[4])
    print("acceler:", acceleration)
    print(current_time)
    #TODO verify that this is the correct units
    #TODO log speed to the log file

    previous_speed = current_speed
    previous_time = current_time

def tirepressure(SingleCanFrame):
    #convert data
    #save to DB table 3
    print("tirepre:", SingleCanFrame.data)

def outsidetemp(SingleCanFrame):
    #convert data
    #save to DB table 4
    print("temp   :", SingleCanFrame.data)

def parse_data(can):
    SingleCanFrame = can

    if SingleCanFrame.arbitration_id == CAR["shifter position"]: #car's shifter position
        shifterposition(SingleCanFrame)

    elif SingleCanFrame.arbitration_id == CAR["speed"]: #car speed
        speed(SingleCanFrame)

    elif SingleCanFrame.arbitration_id == CAR["tire pressure"]: #tire pressure
        tirepressure(SingleCanFrame)

    elif SingleCanFrame.arbitration_id == CAR["outside temp"]: #outside temp
        outsidetemp(SingleCanFrame)

    #else:
        #print("this is the else statement")
        #save to DB errorlog

def count():

    global counter

    # Increment counter by 1
    counter.set(counter.get() + 1)

#####################################################################################################
# MAIN LOOP

# Create the main window
root = tk.Tk()
root.title("LEAF HACK")

# Tkinter variable for holding a counter
counter = tk.IntVar()
counter.set(0)

# Create Widgets
label_counter = tk.Label(root, width=70, textvariable=counter)
button_counter = tk.Button(root, text="Count", command=count)

# Layout Labels
label_counter.pack()
button_counter.pack()

#parse_data(msg)

root.mainloop()



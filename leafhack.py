#this is the leafhack program
import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'can0'
can.rc['bitrate'] = 500000
from can.interfaces.interface import Bus

bus = Bus()

class can.Notifier(can0, <listeners>, timeout=1.0, loop=None)  #TODO need to build list of listeners and fill it in here

can.Notifier.add_bus(can0)

can.Notifier.stop(10) #TODO need to add this to the shutdown sequence

can.BusABC(can0, <can_filters=None, **kwargs) #TODO can I remove "**kwargs"?


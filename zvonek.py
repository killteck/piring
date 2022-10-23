""" Server detekujici aktualni zvoneni a multicasting do lokalni site """
from MulticastHelper import MulticastHelper
import audioop
import pyaudio
import datetime
from time import sleep

def detectSound(multicast, threashold):
    chunk = 1024
    requiredAmountOfPositives = 3   # every 0.25ms -> 

    p = pyaudio.PyAudio()

    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    inputDevices = []
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
            inputDevices.append(i)

    print("numInputDevices ", len(inputDevices))
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=chunk,
                    input_device_index=inputDevices[-1])

    activePositives = 0

    while(True):
        data = stream.read(chunk, exception_on_overflow=False)
        rms = audioop.rms(data, 2)  #width=2 for format=paInt16
        if (rms > threashold):
            activePositives = activePositives + 1
            print("Not silence %s active positives %d" % (datetime.datetime.now(), activePositives))
            if activePositives > requiredAmountOfPositives:
                print('Detected ring')
                multicast.annouce()
                requiredAmountOfPositives = 0
                sleep(5)
        else:
            print(datetime.datetime.now())
            activePositives = 0


if __name__ == '__main__':
    # Choose an arbitrary multicast IP and port.
    # 239.255.0.0 - 239.255.255.255 are for local network multicast use.
    # Remember, you subscribe to a multicast IP, not a port. All data from all ports
    # sent to that multicast IP will be echoed to any subscribed machine.
    multicast_address = "239.0.0.0"
    multicast_port = 6138

    helper = MulticastHelper(multicast_address, multicast_port)

    helper.start(True)

    detectSound(helper, 2)
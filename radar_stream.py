import numpy as np
from loader.radar_sample_reader import radar_sample_reader
import matplotlib.pyplot as plt
import socket

#Import the parameters from the radar setup, edit params.py for different parameters
from params import numADCSamples, numTxAntennas,numRxAntennas, numLoopsPerFrame, numRangeBins

count = 0
if __name__ == '__main__':
    fg = plt.figure()
    ax = fg.gca()

    first_time = True
    im = 0
    # Opening datafile
    # filename = "../2021_02_12_18_40_25.open_radar"
    filename = input("Enter the file name: ")
    filename = "2022_01_19_11_00_31"
    filename = filename + ".open_radar"
    print(filename)
    reader = radar_sample_reader(filename)


    while True:
        # Reading data from file
        try:
            header,np_raw_frame = reader.getNextSample()
        except:
            header,np_raw_frame = radar_sample_reader(filename).getNextSample()
        # print("type:  ", type(np_raw_frame))
        # print("shape: ", np.shape(np_raw_frame))
        # np_raw_frame = np_raw_frame[:round(len(np_raw_frame)/2)]
        print("new length: ", len(np_raw_frame))
        raw_frame = np.array(np_raw_frame, dtype=np.byte)
        # print("-----------")
        # print(header.timestamp)
        # Assuming the data is ready to be processed at this point
        # print("-----------")
        UDP_IP = "127.0.0.1"
        UDP_PORT = 5005
        #print("UDP target IP: %s" % UDP_IP)
        #print("UDP target port: %s" % UDP_PORT)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        # sock.sendto(header, (UDP_IP, UDP_PORT))
        msgSend = str.encode(str(raw_frame))
        # msgSend = str.encode("Test Message")
        print(msgSend)
        sock.sendto(msgSend, (UDP_IP, UDP_PORT))
        """
        for i in range(len(raw_frame)):
            str
            sock.sendto(raw_frame(i), (UDP_IP, UDP_PORT))
	"""

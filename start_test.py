import os
import subprocess

os.chdir('/home/nolan/radar/openradar_mmwave_utils/setup_radar/build')
subprocess.call("./setup_radar", shell=True)

print("Radar Setup")

os.chdir('/home/nolan/radar/openradar_mmwave_utils/setup_dca1000/build')
subprocess.call("./setup_dca1000", shell=True)

print("DCA1000 Setup")

subprocess.call("sudo python /home/nolan/radar/open_radar_processing/receive_and_log_raw_data.py", shell=True)

import psutil
import time
import winsound

UPDATE_DELAY = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil
io = psutil.net_io_counters()
# extract the total bytes sent and received
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

while True:
    winsound.Beep(int(round(psutil.net_io_counters().bytes_recv/40000)), 500)
    winsound.Beep(int(round(psutil.net_io_counters().bytes_sent/40000)), 500)
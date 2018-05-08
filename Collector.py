import shutil
import logging
import psutil
import requests
from uuid import getnode as get_mac
import mmh3
import time

encrypt = 0

mac = get_mac()

if encrypt == 1:
    mac = mmh3.hash(mac.to_bytes(8,'little'))

while True:
    print('START')
    #build cpu points
    cpu_point = f"winstats,counter_name=cpu val={psutil.cpu_percent()}"
    #build net points
    net_io_counter_points = psutil.net_io_counters()
    bytes_sent_point = f"winstats,counter_name=bytes_sent val={net_io_counter_points.bytes_sent/1000000}"
    bytes_recieved_point = f"winstats,counter_name=bytes_recv val={net_io_counter_points.bytes_recv/1000000}"
    packets_sent_point = f"winstats,counter_name=packets_sent val={net_io_counter_points.packets_sent}"
    packets_recv_point = f"winstats,counter_name=packets_recv val={net_io_counter_points.packets_recv}"
    #build mem points
    virtual_memory_points = psutil.virtual_memory()
    total_point = f"winstats,counter_name=total val={virtual_memory_points.total/1000000}"
    available_point = f"winstats,counter_name=available val={virtual_memory_points.available/1000000}"
    #build disk points
    disk_points = psutil.disk_io_counters()
    read_bytes_point = f"winstats,counter_name=disk_read_bytes val={disk_points.read_bytes/1000000}"
    write_bytes_point = f"winstats,counter_name=disk_write_bytes val={disk_points.write_bytes/1000000}"
    write_time_point = f"winstats,counter_name=write_time val={disk_points.write_time}"
    read_time_point = f"winstats,counter_name=read_time val={disk_points.read_time}"
    #send points
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=cpu_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=bytes_sent_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=bytes_recieved_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=packets_sent_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=packets_recv_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=total_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=available_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=read_bytes_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=write_bytes_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=write_time_point)
    req = requests.post("URLPLACEHOLDER:8086/write?db=testdb",
                        data=read_time_point)
    print('END')
    time.sleep(5)

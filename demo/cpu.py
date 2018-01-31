#encoding:utf8
import os
hostname  = os.popen("hostname").read().strip()   #获取主机名

ip = os.popen("ip addr show eth0 |grep inet |awk '{print $2}'|cut -d: -f2").read().strip()
mem = os.popen("free -m |grep Mem |awk '{print $2}'").read().strip()+"M"  #获取内存总量

disk = os.popen("fdisk -l |grep -E Disk |awk '{print $3}'").read().strip()+"G" #获取硬盘总大小
print(hostname,mem,disk,ip)

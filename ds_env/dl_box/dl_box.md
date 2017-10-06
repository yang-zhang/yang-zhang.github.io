# Deep Learning Box Setup

## Hardware
Tips:
- RAM 2x the size of GPU memory
- Motherboard and case the same type (e.g., Mini ITX)

My [part list](https://pcpartpicker.com/list/jcM9kT):

![](https://github.com/yang-zhang/yang-zhang.github.io/blob/master/ds_env/dl_box/dl_box.png)

- CPU: Intel - Core i5-6500 3.2GHz Quad-Core Processor 
- Motherboard: MSI - B250I GAMING PRO AC Mini ITX LGA1151 Motherboard 
- Memory: Corsair - Vengeance LPX 16GB (2 x 8GB) DDR4-3000 Memory 
- Storage: Seagate - Barracuda 3TB 3.5" 7200RPM Internal Hard Drive 
- Video Card: EVGA - GeForce GTX 1060 6GB 6GB GAMING Video Card  ($309.00 @ Adorama) 
- Case: Thermaltake - Core V1 Mini ITX Tower Case 
- Power Supply: Corsair - CSM 550W 80+ Gold Certified Semi-Modular ATX Power Supply 

![](https://github.com/yang-zhang/yang-zhang.github.io/blob/master/ds_env/dl_box/dl_box_parts.jpg)

References
- http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/
- https://youtu.be/cRjPVN3oo4s?t=1981
- https://blog.slavv.com/the-1700-great-deep-learning-box-assembly-setup-and-benchmarks-148c5ebe6415
- http://forums.fast.ai/t/making-your-own-server/174
- https://medium.com/towards-data-science/building-your-own-deep-learning-box-47b918aea1eb
- https://www.oreilly.com/learning/build-a-super-fast-deep-learning-machine-for-under-1000
- https://pcpartpicker.com/
- https://superuser.com/questions/1186150/gpu-memory-bandwidth-vs-speed
- http://graphific.github.io/posts/building-a-deep-learning-dream-machine/
- https://medium.com/@timcamber/deep-learning-pc-build-5cffa71ad97 
- https://medium.com/towards-data-science/build-a-deep-learning-rig-for-800-4434e21a424f

## Software

### OS
Create a bootable Ubuntu USB stick.

Reference:
- https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos

### GPU Driver
Install cuda driver before installing graphic card:
```sh
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```
Add to `~/.bash_profile':
```sh
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LIBRARY_PATH:+:${LIBRARY_PATH}}
```
References:
- https://medium.com/towards-data-science/building-your-own-deep-learning-box-47b918aea1eb
- https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork

### Setup ssh

Find out default gateway using `route -n`. For example `192.168.1.1`. Go to this IP in browser, end username and password (e.g., `admin`, `admin`).
Find out inet addr using `ifconfig`. For example `192.168.1.114`, enable Port `22` for this IP.


```sh
sudo apt-get install openssh-server
sudo service ssh status
```
References:
- https://askubuntu.com/questions/140236/can-i-access-my-home-pc-from-the-office-with-ssh
- https://www.pcworld.com/article/244314/how_to_forward_ports_on_your_router.html
- http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/


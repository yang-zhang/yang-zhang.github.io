# GPU Box

## Hardware

## Software

[here](https://medium.com/towards-data-science/building-your-own-deep-learning-box-47b918aea1eb)
and [here](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork)

```sh
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```

## References
- http://timdettmers.com/2017/04/09/which-gpu-for-deep-learning/
- https://youtu.be/cRjPVN3oo4s?t=1981
- https://blog.slavv.com/the-1700-great-deep-learning-box-assembly-setup-and-benchmarks-148c5ebe6415
  - SSD: I remember when I got my first Macbook Air years ago, how blown away was I by the SSD speed. To my delight, a new generation of SSD called NVMe has made its way to market in the meantime. A 480 GB MyDigitalSSD NVMe drive for $230 was a great deal. This baby copies files at gigabytes per second.
  - The one thing that I kept in mind when picking a motherboard was the ability to support two GTX 1080 Ti, both in the number of PCI Express Lanes (the minimum is 2x8) and the physical size of 2 cards. Also, make sure it’s compatible with the chosen CPU. An Asus TUF Z270 for $130 did it for me. MSI — X99A SLI PLUS should work great if you got an Intel Xeon CPU.
  - Deepcool 750W Gold PSU for $75. 
  - The case should be the same form factor as the motherboard. Also having enough LEDs to embarrass a Burner is a bonus. A friend recommended the Thermaltake N23 case for $50, 
- http://forums.fast.ai/t/making-your-own-server/174
- https://medium.com/towards-data-science/building-your-own-deep-learning-box-47b918aea1eb
    - CPU — Intel i7 7700k 4.2GHz Quad-Core $343
    - RAM — Corsair Vengeance LPX 32GB (2 x 16) DDR4–3200 $276
    - SSD—Samsung 850 EVO-Series 500GB $160
    - GPU — Zotac GeForce GTX 1080 8GB AMP! Edition $565
    - Motherboard — MSI Z270-A PRO ATX LGA1151 $114
    - Cooler — Cooler Master Hyper 212 EVO 82.9 CFM $28
    - Power Supply — EVGA SuperNOVA G2 750W ATX $100
    - Case — NZXT S340 (White) ATX Mid Tower Case $70
    - Total: $1,654
- https://www.oreilly.com/learning/build-a-super-fast-deep-learning-machine-for-under-1000
  - ASUS Mini ITX DDR4 LGA 1151 B150I PRO GAMING/WIFI/AURA Motherboard for $125 on Amazon. It comes with a WiFi antenna, which is actually super useful in my basement.
  - The size should match the motherboard, so it needs to have mini-ITX in the name. I bought a Thermaltake Core V1 Mini ITX Cube on Amazon for $50.
- https://pcpartpicker.com/
- https://superuser.com/questions/1186150/gpu-memory-bandwidth-vs-speed
- http://graphific.github.io/posts/building-a-deep-learning-dream-machine/
 - Also make sure the CPU supports 40 PCIe lanes, some new Haswell CPUs only support 32;
 - Get twice the amount of RAM as your total GPU memory;
 - SSD is nice but only an absolute necessity if you load datasets which don’t fit into GPU memory and RAM combined. If you do get an SSD, get at least one larger than your largest datase
- https://medium.com/@timcamber/deep-learning-pc-build-5cffa71ad97 
- https://medium.com/towards-data-science/build-a-deep-learning-rig-for-800-4434e21a424f
  - under 800

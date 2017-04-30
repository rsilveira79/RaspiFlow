# RaspiFlow
Computer vision testing with Raspberry Pi 3 and Tensorflow

## Testing Camera Stream to other Computer

1. Install VLC on Rpi

```
sudo apt-get install vlc
```

2. Run VLC command to stream camera

```
raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
```

3. Open VLC on other machine (Win) --> Media --> Open Network Stream --> http://[Rpi 3 IP Address]:[Stream Port = 8160]

## RPi-Cam Web Interface - nice web-interface to Rpi camera streaming

[RPi-Cam-Web-Interface](http://elinux.org/RPi-Cam-Web-Interface)

## To take pictures (native testing)
```
raspistill -o image.jpg
```


## Installing dlib on Rpi

1. Install dependencies

```
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
$ sudo pip3 install numpy
$ sudo pip3 install scipy
$ sudo pip3 install scikit-image
```
2. Increase swap file to 400 MB
```
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo nano /etc/dphys-swapfile
CONF_SWAPSIZE=400
$ sudo /etc/init.d/dphys-swapfile start
```
3. Decrease GPU memory on Rpi
```
$ sudo raspi-config
Advanced Option --> Memory Split --> 16
```

4. Install dlib
```
$ sudo pip3 install dlib
```

5. Return swap file to 100/200 MB
```
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo nano /etc/dphys-swapfile
$ modify line --> CONF_SWAPSIZE=200
$ sudo /etc/init.d/dphys-swapfile start
```

6. Increase GPU memory on Rpi
```
$ sudo raspi-config
Advanced Option --> Memory Split --> 128
```

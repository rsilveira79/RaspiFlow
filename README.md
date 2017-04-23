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

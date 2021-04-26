# omxplayer-wrapper

Just a small wrapper demon script for omxplayer.  
This script should run permanently in background. (e.g. screen)

## Getting started

1. Clone this repository: `git clone https://github.com/MaaxGr/omxplayer-wrapper.git omxplayer-wrapper`
1. `cd omxplayer-wrapper`
1. Create a new screen `screen -S omxplayer-wrapper`
1. Run the script inside the screen: `python3 omx-wrapper.py`
1. Leave the screen
1. Run `omx-run.py` script, to send commands to omxplayer

## Commands

|Action|Command|
|---|---|
|Start playing a local sound file|`python omx-run.py play:/root/Music/tvk/tvk_intotheunknown.mp3`|
|Stop playing local sound file|`python omx-run.py stop`|

All other run-commands will be directly passed to omxplayer stdin.
For an overview of all key-bindings/commands, see [omxplayer github repository](https://github.com/popcornmix/omxplayer#key-bindings).

These are in my opinion the most import ones:

|Action|Command|
|---|---|
|Pause/Resume|`python omx-run.py p`|
|Increase volume|`python omx-run.py +`|
|Decrease volume|`python omx-run.py -`|
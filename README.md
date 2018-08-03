# Pin 
[![Build Status](https://travis-ci.org/fedeb95/pin.png?branch=master)](https://travis-ci.org/fedeb95/pin)
[![Coverage](https://codecov.io/gh/fedeb95/pin/branch/master/graph/badge.svg)](https://codecov.io/fedeb95/pin/)
  
RPi.GPIO wrapper. Write code once, test it anywhere, run on Raspberry Pi

<h2>Why<h2>
  
I wanted to test some ideas I had in mind for my Raspberry Pi, but I didn't have it with me. 
So I made this really tiny library which acts as a wrapper for RPi.GPIO. You can write your code on your laptop, test it and then deploy it on your Raspberry Pi by only changing a value in a configuration file, only when it's really working.

<h2>How</h2>

First create a config file with this content:

```
{
  "test":true
}
```

This enables the mocking. If you're executing your script on a anctual raspberry you may want to set `'test'` to `false`. This transforms every call to an actual GPIO call.

Now load your configuration file:

```
pin.config('/path/to/config/file')
```

Then you are ready to interact with the library exactly how you'd do with Rpi.GPIO:
```
pin.setmode(pin.BCM)
pin.setup(4,pin.OUT)
pin.output(4,pin.LOW)
```

The file and the call to `config()` are mandatory, since apparently `RPi.GPIO` can't be imported on a system that's not a Raspberry Pi. So the method also imports the module if the `"test"` value is `false`.

You may see a `pin.conf` dictionary and be tempted to set `"test"` there without an external file, and without calling `config()`. This way RPi.GPIO isn't imported and your code won't work on an actual Raspberry Pi. Use at your own risk.

What if you want your pin to read an input?

```
pin.setup(4,pin.IN)
value = pin.input(4)
```

This returns a random value.
If you want to control the value read you can use `pin.set_value()`:

```
# before starting your script
pin.set_value(4,0.5)
# your script
value = pin.input(4)
```
 
This way other applications can be built. For instance a GUI that simulates a Raspberry with devices attached.

<h2>Dependencies</h2>
You need to install RPi.GPIO for this to work
https://sourceforge.net/p/raspberry-gpio-python/wiki/install/

In test mode this isn't required since RPi.GPIO isn't imported.

Tested under Python 3.6

<h2>Installation</h2>
Clone this repository, then run

```
python3 setup.py install
```

<h2>What's implemented of RPi.GPIO</h2>

* `setup(channel,in_or_out,initial=pin.HIGH)` same as GPIO, works also with a list of channels. Use `pin.IN` or `pin.OUT`, as well as `pin.HIGH` or `pin.LOW`
* `setmode(mode)` same as GPIO, use `pin.BCM` or `pin.BOARD`. In test mode this won't do anything.
* `input(channel)` same as GPIO, if `pin.set_value(channel,value)` isn't called before then a random number in range [0,1] is returned. Otherwise what you set with `set_value()` for that channel
* `output(channel,value)` same as GPIO, writes `value` to pin `channel`. In test mode you can retrieve what was set with `pin.get_output(channel)`. You may use `pin.HIGH` or `pin.LOW`. As `setup()` works with a list of channels
* `cleanup(channel)` same as GPIO, works also with a list of channels

<h2>Additional functions</h2>
This functions are only useful in test mode. See `test` folder for better examples.

* `set_value(channel,value)` every time `input(channel)` is called, `value` is returned instead of a random number
* `get_output(channel)` returns whatever `output(channel,value)` wrote to `channel`

<h2>The future</h2>
People actually serious with their Raspberries, please let me know of improvement or whatever you may find useful. I use mine as an hobby, and I'm not an expert of IoT. Any contribution is welcomed basically.

Since I haven't found a way to properly and automatically test this library behaviour on a Rapsberry, either tell me how or report issues about the actual RPi.GPIO calls. What this library is trying to solve is exactly this apparent difficulty of testing Raspberry code properly.

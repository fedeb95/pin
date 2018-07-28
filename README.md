# Pin
Library for mocking Rpi.GPIO transparently.

<h1>Attention: this does not yet work as intended. It will be in a few days, I can't make private repositories.</h1>

<h2>History</h2>

I wanted to test some ideas I had in mind for my Raspberry Pi, but I didn't have it with me. 
So I made this really tiny library which acts as a wrapper for RPi.GPIO.

<h2>Usage Example</h2>

First create a config file with this content:

```
{
  'test':true
}
```

This enables the mocking. If you're executing your script on a anctual raspberry you may want to set `'test'` to `false`.

Then you are ready to interact with the library exactly how you'd do with Rpi.GPIO:
```
pin.config('/path/to/config/file') 
pin.setmode(pin.BCM)
pin.setup(4,pin.OUT)
pin.output(4,pin.LOW)
```

The file and the call to `config()` are mandatory, since apparently `RPi.GPIO` can't be imported on a system that's not a Raspberry Pi. So the method also imports the module if the `'test'` value is `False`.

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

<h2>Dependencies</h2>
You need to install RPi.GPIO for this to work
https://sourceforge.net/p/raspberry-gpio-python/wiki/install/


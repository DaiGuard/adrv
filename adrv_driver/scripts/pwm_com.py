#!/usr/bin/env python


import Adafruit_PCA9685


class PWMCom:

  def __init__(self, port=0, hz=50.0):
    """
    Initialize PWMCom class

    Args:
      port: int
        i2c port number
      hz: float
        pwm frequency
    """

    #----------------------#
    # Initialize member values
    self._port = port
    self._hz = hz
    self._ch_params = {}

    #----------------------#
    # Initialize PWM setting
    self._pwm = Adafruit_PCA9685.PCA9685()    
    self._pwm.set_pwm_freq(self._hz)


  def __del__(self):
    pass
  
  def InitPWM(self, ch, min, max):
    """
    Initialize PWM Output

    Args:
      ch : int
        initialize pwm channel
      min : float
        minimum pwm on time (ms)
      max : float
        maximum pwm on time (ms)
        
    Returns:
      bool:
        result of initialize pwm task.
        True: success
        False: faulse
      str:
        result message  
    """

    bmin = int(min / ((1.0 /self._hz) / 4096))
    bmax = int(max / ((1.0 /self._hz) / 4096))

    #----------------------#
    # value error check
    if bmin < 0 or bmin > 4096:      
      return False, 'Overflow minimu pwm on time'
    if bmax < 0 or bmax > 4096:
      return False, 'Overflow maximum pwm on time'
    if bmin > bmax:
      return False, 'Minimum value is greater than maximum value'    
    if ch < 0:
      return False, 'Out of range channel value'    

    self._ch_params[ch] = [bmin, bmax]
    self._pwm.set_pwm(ch, 0, (bmin+bmax)/2)

    print '-----------------'
    print 'CH: %d Initialize' % ch
    print '  min: %d, max: %d' % (bmin, bmax)

    return True, ""


  def SetPWM(self, ch, ratio):
    """
    """

    if ratio < -1.0:
      return False, "Out of range ratio"
    if ratio > 1.0:
      return False, "Out of range ratio"
    if ch < 0:
      return False, 'Out of range channel value'

    [bmin, bmax] = self._ch_params[ch]

    pulse = int((bmax + bmin) / 2.0 + (bmax - bmin) / 2.0 * ratio)

    self._pwm.set_pwm(ch, 0, pulse)

    print "[" + str(ch) +"]: " + str(pulse) + " ( " + str(bmin) + " / " + str(bmax) + " )"
    
    return True, ""
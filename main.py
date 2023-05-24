from phue import Bridge
import time


def main():
    bridge = Bridge('192.168.1.3')
    bridge.connect()   
    bridge.get_api()

    lights = bridge.lights

    # for l in lights:
    #     print(l.name)


    # print("This is a test")

    bridge.get_light('Desk-10')
    #command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
    command = {"on":True, "sat":254, "bri":254,"hue":666}
    bridge.set_light('Desk-10', 'on', False)
    bridge.set_light('Desk-10', command)
    time.sleep(5)

    command = {"on":True, "sat":254, "bri":254,"hue":22695}
    bridge.set_light('Desk-10', 'on', False)
    bridge.set_light('Desk-10', command)
    time.sleep(5)

    command = {"on":True, "sat":254, "bri":254,"hue":46920}
    bridge.set_light('Desk-10', 'on', False)
    bridge.set_light('Desk-10', command)
    
if __name__ == "__main__":
    main()

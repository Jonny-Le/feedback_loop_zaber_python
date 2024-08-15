import zaber_driver
import gui

def main():
    zaber_device = zaber_driver.zaber_connect()
    gui.create_gui(zaber_device)
    
if __name__ == "__main__":
    main()
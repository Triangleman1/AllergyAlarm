import asyncio
import signal
from bleak import BleakClient, BleakScanner

# list of BLE names
CORSENSE_NAME = "CorSense B-05384"
POLAR_H9_NAME = "Polar H9 77B0D721"
POLAR_H10_NAME = "Polar H10 75340F2C"
POLAR_OH1_NAME = "Polar OH1 83D5862B"
POLAR_SENSE_NAME = "Polar Sense A56A6B22"
BIOSTRAP_CHEST_STRAP_NAME = "HRM 0006268"

# list of BLE characteristics
HEARTRATE_CHARACTERISTIC = "00002a37-0000-1000-8000-00805f9b34fb"

# choose which name and characteristic to use
NAME_CHOICE = BIOSTRAP_CHEST_STRAP_NAME
CHARACTERISTIC_CHOICE = HEARTRATE_CHARACTERISTIC

def heartrate_callback(sender: int, data: bytearray):
    index = 1
    measurement = list(data)


    if measurement[0] & 0x01 == 0x01:
        print(f"Heart Rate: {int.from_bytes(measurement[index:index+2], byteorder='little')} bpm")
        index += 2
    else:
        print(f"Heart Rate: {measurement[index]} bpm")
        index += 1

    if measurement[0] & 0x04 == 0x04:
        if measurement[0] & 0x02 == 0x02:
            print("Sensor contact detected")
        else:
            print("No or poor sensor contact detected")

    if measurement[0] & 0x08 == 0x08:
        print(f"Energy expended: {int.from_bytes(measurement[index:index+2], byteorder='little')} kilojoules")
        index += 2

    if measurement[0] & 0x10 == 0x10:
        for i in range(index, len(measurement), 2):
            print(f"RR interval {i-index+1}: {int.from_bytes(measurement[i:i+2], byteorder='little')/1024} seconds")

async def main():
    devices = await BleakScanner.discover()
    target_device = None

    for device in devices:
        if device.name == NAME_CHOICE:
            print("Found target device: ", device.name)
            target_device = device
            break

    if not target_device:
        print(f"Device {NAME_CHOICE} not found!")
        return
    
    async with BleakClient(target_device.address, timeout=60) as client:
        print("Device connected. Starting notifications...")

        await client.start_notify(CHARACTERISTIC_CHOICE, heartrate_callback)

        stop_event = asyncio.Event()

        def signal_handler(sig, frame):
            stop_event.set()

        signal.signal(signal.SIGINT, signal_handler)

        try:
            while not stop_event.is_set():
                await asyncio.sleep(0)
        except asyncio.CancelledError or Exception:
            pass

        await client.stop_notify(CHARACTERISTIC_CHOICE)
        print("Stopped notifications.")
        return

if __name__ == "__main__":
    asyncio.run(main())
from serial import Serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())

#Windows code for figuring out which port to grab

for port in ports:
    if "DF60BCA" in port.hwid and port.pid == 33032:
        print("FOUND MACROPAD!")
        ser = Serial(port.name)
        ser.write(b"hello!\n")
        line = ser.readline()
        print(line)
        print(line.decode("utf-8"))
        line = ser.readline()
        print(line)
        print(line.decode("utf-8"))
        line = ser.readline()
        print(line)
        print(line.decode("utf-8"))
        line = ser.readline()
        print(line)
        print(line.decode("utf-8"))

        ser.close()




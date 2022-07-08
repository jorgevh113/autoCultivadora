 #String json_data = "{\"Sesor_id\":\"3E24R\",\"Value\":" + (String)randNumber + "}";

import serial, time, json

hw_sensor = serial.Serial(port='COM8', baudrate=115200, timeout=1, write_timeout=1)

if __name__ == '__main__':
    while True:
        hw_sensor.write('getValue'.encode('utf-8'))
        time.sleep(1)
        try:
            raw_string_b = hw_sensor.readline()
            raw_string_s = raw_string_b.decode('utf-8')
            if(raw_string_s.index("}")>=0 and raw_string_s.index("{")==0):
                raw_string_s = raw_string_s[0:raw_string_s.index("}")+1]
                raw_string_j = json.loads(raw_string_s)
                print(raw_string_j)
                print(raw_string_j["Sensor_id"])
                print(raw_string_j["Value"])
            else:
                print("error/ no } found.")
        except:
            print("Exception occurred, somthing wrong...")
    hw_sensor.close()
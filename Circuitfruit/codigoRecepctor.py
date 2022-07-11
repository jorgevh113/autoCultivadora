import supervisor

def serial_read():
   if supervisor.runtime.serial_bytes_available():
       value = input()
       print(value)
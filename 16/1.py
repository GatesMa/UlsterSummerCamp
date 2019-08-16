raw_temp_data = '8c 0a c0 0d'
raw_temp_bytes = raw_temp_data.split()
raw_ambient_temp = int('0x' + raw_temp_bytes[3] + raw_temp_bytes[2], 16)
ambient_temp_int = raw_ambient_temp >> 2 & 0x3FFF
ambient_temp_celsius = float(ambient_temp_int) * 0.03125
ambient_temp_fahrenheit = (ambient_temp_celsius * 1.8) +32

print('Celsius:')
print(ambient_temp_celsius)
print('Fahrenheit:')
print(ambient_temp_fahrenheit)


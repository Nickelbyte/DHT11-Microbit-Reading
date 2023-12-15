def on_forever():
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P2, True, True, True)
    basic.show_number(50 + pins.analog_read_pin(AnalogPin.P1) / 25)
    print(50 + pins.analog_read_pin(AnalogPin.P1) / 25)
    if dht11_dht22.read_data(dataType.TEMPERATURE) > 50 + pins.analog_read_pin(AnalogPin.P1) / 25 + 2:
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.servo_write_pin(AnalogPin.P8, 90)
    elif dht11_dht22.read_data(dataType.TEMPERATURE) < 50 + pins.analog_read_pin(AnalogPin.P1) / 25 - 2:
        pins.servo_write_pin(AnalogPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P15, 0)

basic.forever(on_forever)